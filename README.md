# Материалы для изучения языка Kotlin

## Особенности сборки

1. Материалы конспектов должны быть выполнены в разметке markdown.
2. Материалы размещаются в директории [docs](./docs).
3. Вставка изображений должна быть выполнена с применением ссылок стандартного синтаксиса markdown c использованием inline-стилей MkDocs-material:
  
  ```markdown
  ![](./images/1_1.png){: style="width:100px"}
  ```
  
  Для конвертации тегов вставки изображений HTML в ссылки markdown можно воспользоваться [скриптом](./utils/image_insertion_converter.py). 
  Скрипт применяется рекурсивно ко всем `*.md` файлам в директории `docs`.

## Инструкция к сборке статического сайта в MkDocs

Запуск локального сервера с собранным сайтом:

```bash
mkdocs serve
```

### Деплой сайта на GitHub Pages.

Бесплатный деплой на GitHub Pages выполняется только для публичных репозиториев.

```bash
mkdocs gh-deploy
```

## Инструкция по сборке в PDF с Docker

1. Загрузить [Docker](https://www.docker.com/) и выполнить перезагрузку.
2. Создать файл `dockerfile` с содержимым ([источник 1](https://github.com/orzih/mkdocs-with-pdf/issues/137), 
   [источник 2](https://github.com/alpinelinux/docker-alpine/issues/181)):

    ```
    FROM squidfunk/mkdocs-material
    
    RUN apk add --no-cache build-base ttf-freefont \
      && apk add --no-cache --virtual libffi-dev-3.2.1-r6 zlib-dev libwebp-dev jpeg-dev harfbuzz-dev fribidi-dev freetype-dev cairo-dev musl-dev pango-dev gdk-pixbuf-dev \
      && pip install mkdocs-with-pdf
    ```
   
3. Открыть терминал и перейти в папку с файлом `dockerfile`.
4. Создать docker образ командой:

    ```bash
    docker build . --tag mkdocs-with-pdf
    ```

5. Отредактировать `mkdocs.yml` чтобы включить в нём сборку сайта в PDF-файл.
6. Запустить сборку сайта уже с нашим с образом
    
    ```bash
    docker run --rm -it -v ${PWD}:/docs mkdocs-with-pdf build
    ```

## Инструкция по сборке в HTML

TODO

Разработано на Python 3.10.11.