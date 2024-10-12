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
2. Создать файл `dockerfile` с содержимым:

    ```
    FROM squidfunk/mkdocs-material
    RUN apk add build-base ttf-ubuntu-font-family libffi-dev zlib-dev 
      libwebp-dev jpeg-dev harfbuzz-dev fribidi-dev freetype-dev 
      cairo-dev musl-dev pango-dev gdk-pixbuf-dev 
      && pip install mkdocs-with-pdf
    ```
   
3. Открыть терминал и перейти в папку с файлом `dockerfile`.
4. Создать docker образ командой:

    ```bash
    docker build . -t metanit_kotlin_abstract
    ```

5. Отредактировать `mkdocs.yml` чтобы включить в нём сборку сайта в PDF-файл.
6. Запустить сборку сайта уже с нашим с образом
    
    ```bash
    docker run --rm -it -v ${PWD}:/docs metanit_kotlin_abstract build
    ```

## Инструкция по сборке в HTML

TODO

Разработано на Python 3.10.11.