FROM balenalib/raspberry-pi:latest-build

RUN install_packages libraspberrypi-bin libraspberrypi-dev checkinstall pkgconf autoconf automake autopoint pkgconf libtool libjpeg9-dev build-essential libzip-dev gettext libmicrohttpd-dev

# It's important that pkgconf is installed so FFmpeg creates pkg-config files that are picked up by the Motion "configure" step

# Install https://github.com/FFmpeg/FFmpeg with h264_omx support
ENV FFMPEG_VERSION=4.4
RUN curl -L -o ffmpeg.tar.bz2 https://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.bz2 \
    && tar -xf ffmpeg.tar.bz2 \
    && rm ffmpeg.tar.bz2 \
    && ( \
        cd ffmpeg-${FFMPEG_VERSION} \
        # use "--extra-libs=-latomic" on "buster" (https://stackoverflow.com/a/62501876/244640)
        && ./configure --arch=armel --target-os=linux --extra-ldflags=-latomic --enable-gpl --enable-mmal --enable-omx --enable-omx-rpi --enable-nonfree \
        && make -j$(nproc) \
        && checkinstall --fstrans=no -y --pkgversion=7:4.1 --provides=ffmpeg,libavutil56,libavcodec58,libavformat58,libavdevice58,libavfilter7,libswscale5,libswresample3,libpostproc5 \
        && dpkg -I *.deb \
    ) \
    && rm -rf ffmpeg-${FFMPEG_VERSION} 

# Install https://motion-project.github.io/ with h264_omx support
ENV MOTION_VERSION=4.3.2
RUN git clone https://github.com/Motion-Project/motion.git \
  && ( \
    cd motion \
    && git checkout "release-${MOTION_VERSION}" \
    && autoreconf -fiv \
    && LDFLAGS=-latomic ./configure \
    && make -j$(nproc) \
    && checkinstall --fstrans=no -y --pkgversion="${MOTION_VERSION}" --provides=motion \
    && dpkg -I *.deb \
  ) \
  && rm -rf motion

COPY motion.conf /etc/motion/motion.conf

EXPOSE 8080
EXPOSE 80/tcp
EXPOSE 80/udp

CMD motion -c /etc/motion/motion.conf

# Set timezone
RUN ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime \
    && dpkg-reconfigure tzdata
