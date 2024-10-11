import os
import re


class ImageInsertionConverter:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = input_dir
        self.output_dir = output_dir

        self.input_files = self.find_md_files(self.input_dir)

    @staticmethod
    def find_md_files(dir: str) -> list[str]:
        """Рекурсивный поиск всех файлов *.md"""
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

        tag_pattern = r'<img\s+src="([^"]+)"\s+width="(\d+)"\s*/>'

        def replace_img(match):
            src = match.group(1)    # Получаем src из совпадения
            width = match.group(2)  # Получаем width из совпадения
            return f'![]({src}){{: style="width:{width}px"}}'

        for file in input_files:
            with open(file, 'r', encoding='utf-8') as markdown:
                content = markdown.read()

            new_content = re.sub(tag_pattern, replace_img, content)

            if rewrite:
                with open(file, 'w', encoding='utf-8') as markdown:
                    markdown.write(new_content)
            else:
                with open(file.replace(".md", "") + "_result.md", 'w', encoding='utf-8') as markdown:
                    markdown.write(new_content)


    def ref_to_tag(self):
        """Конвертация ссылки markdown c использованием inline-стилей MkDocs-material в html-тег."""
        # for file in self.input_files:
        pass


