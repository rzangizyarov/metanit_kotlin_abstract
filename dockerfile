FROM squidfunk/mkdocs-material
RUN apk add build-base ttf-ubuntu-font-family libffi-dev zlib-dev
  libwebp-dev jpeg-dev harfbuzz-dev fribidi-dev freetype-dev
  cairo-dev musl-dev pango-dev gdk-pixbuf-dev
  && pip install mkdocs-with-pdf