FROM golang:1.15-alpine
RUN apk add --no-cache git inotify-tools \
  && (GO111MODULE=on go get github.com/gphotosuploader/gphotos-uploader-cli) \
  && apk del git
COPY user/.gphotos-uploader-cli /root/.gphotos-uploader-cli
CMD ["/bin/sh", "-c", \
  "while true ; do \
    gphotos-uploader-cli push ; \
    inotifywait -e close_write -e move /safaricam/media/Safaricam ; \
  done"]
