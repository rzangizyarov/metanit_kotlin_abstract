FROM squidfunk/mkdocs-material

RUN apk add --no-cache build-base ttf-freefont \
  && apk add --no-cache --virtual libffi-dev-3.2.1-r6 zlib-dev libwebp-dev jpeg-dev harfbuzz-dev fribidi-dev freetype-dev cairo-dev musl-dev pango-dev gdk-pixbuf-dev \
  && pip install mkdocs-with-pdf