import os
import re


class ImageInsertionConverter:

    @staticmethod
    def find_md_files(dir: str) -> list[str]:
        """Рекурсивный поиск всех файлов *.md в указанной папке"""
        md_files = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    md_files.append(os.path.join(root, file))
        return md_files

    @staticmethod
    def tag_to_ref(input_files: list[str], rewrite: bool = True):
        """Конвертация html-тега в ссылку markdown c использованием inline-стилей MkDocs-material."""
        tag_pattern = r"""<img\s+src=["']([^"']+)["']\s+width=["'](\d+)["']\s*(\/>|><\/img>)"""

        def replace_tag(match):
            src = match.group(1)    # Получаем src из совпадения
            width = match.group(2)  # Получаем width из совпадения
            return f'![]({src}){{: style="width:{width}px"}}'

        for file in input_files:
            with open(file, 'r', encoding='utf-8') as markdown:
                content = markdown.read()

            new_content = re.sub(tag_pattern, replace_tag, content)

            if rewrite:
                with open(file, 'w', encoding='utf-8') as markdown:
                    markdown.write(new_content)
            else:
                with open(file.replace(".md", "") + "_result.md", 'w', encoding='utf-8') as markdown:
                    markdown.write(new_content)

    @staticmethod
    def ref_to_tag(input_files: list[str], rewrite: bool = True):
        """Конвертация ссылки markdown c использованием inline-стилей MkDocs-material в html-тег."""
        markdown_pattern = r'!\[\]\(([^)]+)\)\{: style="width:(\d+)px"\}'

        def replace_ref(match):
            src = match.group(1)    # Получаем src из совпадения
            width = match.group(2)  # Получаем width из совпадения
            return f'<img src="{src}" width="{width}"/>'

        for file in input_files:
            with open(file, 'r', encoding='utf-8') as markdown:
                content = markdown.read()

            new_content = re.sub(markdown_pattern, replace_ref, content)

            if rewrite:
                with open(file, 'w', encoding='utf-8') as markdown:
                    markdown.write(new_content)
            else:
                with open(file.replace(".md", "") + "_result.md", 'w', encoding='utf-8') as markdown:
                    markdown.write(new_content)


if __name__ == "__main__":
    image_insertion_converter = ImageInsertionConverter()

    image_insertion_converter.tag_to_ref(
        input_files=image_insertion_converter.find_md_files("../docs"),
    )

    # image_insertion_converter.ref_to_tag(
    #     input_files=image_insertion_converter.find_md_files("../docs"),
    # )
