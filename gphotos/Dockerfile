FROM golang:1.16-alpine AS build
RUN apk add --no-cache --update alpine-sdk tar
ADD https://github.com/gphotosuploader/gphotos-uploader-cli/archive/refs/tags/v3.1.0.tar.gz gphotos-upload-cli.tar.gz
RUN tar xzf gphotos-upload-cli.tar.gz
RUN cd gphotos-uploader-cli-3.1.0 && make build

FROM alpine:3.14
COPY --from=build /go/gphotos-uploader-cli-3.1.0/gphotos-uploader-cli /bin/gphotos-uploader-cli
COPY user/.gphotos-uploader-cli /root/.gphotos-uploader-cli
CMD ["/bin/sh", "-c", \
  "while true ; do \
    /bin/gphotos-uploader-cli push ; \
    inotifywait -e close_write -e move /safaricam/media/Safaricam ; \
  done"]
