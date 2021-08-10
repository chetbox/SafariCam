from datetime import date, datetime, timedelta
import pytz
import astral
from astral.sun import sun as Sun
import pause
import RPi.GPIO as GPIO

def now():
  return datetime.now(pytz.UTC)

def sunrise_sunset(now):
  city = astral.LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
  sun = Sun(city.observer,  date=now)
  return sun['sunrise'], sun['sunset']

def next_sunrise_or_sunset(now):
  return min([
    time for time in 
    sunrise_sunset(now) + sunrise_sunset(now + timedelta(days=1))
    if time > now
  ])

def is_daytime(now):
  sunrise, sunset = sunrise_sunset(now)
  return now >= sunrise and now < sunset

def main(ir_led_pin=7):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ir_led_pin, GPIO.OUT)

  was_daytime = None

  while True:
    if is_daytime(now()):
      if was_daytime != True:
        # It's now day time
        print('Turning LED off')
        GPIO.output(ir_led_pin, True)
      was_daytime = True
    else:
      if was_daytime != False:
        # It's now night time
        print('Turning LED on')
        GPIO.output(ir_led_pin, False)
      was_daytime = False
    pause.minutes(30)

if __name__ == "__main__":
  main()
