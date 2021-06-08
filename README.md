# SafariCam

A Raspberry Pi Zero-based motion detection camera desiged for capturing animals outdoors.

Runs on [Balena Cloud]

## Hardware

- Raspberry Pi Zero W
- [IR-CUT](https://thepihut.com/products/raspberry-pi-night-vision-camera-ir-cut) Night vision camera

## How to use

- Create a Balena Cloud project called `SafariCam`
- Add the Raspberry Pi and installed the Balena Cloud SD card image. Don't forget to set WiFi details if you don't have a wired network connection.
- Clone this repo
- Run `balena push SafariCam`

## Google Photos upload

Uses a "Device Service Variable" set on Balena Cloud called `GPHOTOS_CLI_TOKENSTORE_KEY` set on the `gphotos` service. This is the password used for storing local credentials. 

This allows safely storing an access token in a public repo as long as this password is not stored in the repo.

To reauthenticate, follow these steps on your local machine:

- Delete the `@gmail.com` file from `gphotos`
- docker run -ti --rm=true -v`pwd`/gphotos/user:/root -v`pwd`/photo:/safaricam/media/Safaricam -e GPHOTOS_CLI_TOKENSTORE_KEY=YOUR_PASSWORD_HERE gphotos /bin/sh
- Run `gphotos-uploader-cli push` and follow the instruction to reauthenticate.
- `Ctrl`+`D` to quit the Docker shell
- Commit the updated file. You can remove the other new files created.
- Update balena cloud with `balena push SafariCam`

## Night Vision

### Automatic

Connect Raspberry Pi GPIO pin 7 (GPIO 4) to the infra-red control pin on the IR-CUT camera to set "night vision" mode automatically. (Assumes `Europe/London` timezone)

### Fixed

Alternatively, to set the infra-red lights to a constant value set `BALENA_HOST_CONFIG_disable_camera_led` to `1` in "Device Configuration" on Balena Cloud to enable "night vision" mode.

This will set `disable_camera_led=1` in `/boot/config.txt`.
