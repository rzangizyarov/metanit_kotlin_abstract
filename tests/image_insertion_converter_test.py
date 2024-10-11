import unittest

from utils.image_insertion_converter import ImageInsertionConverter


class ImageInsertionConverterTest(unittest.TestCase):
    def setUp(self):
        self.image_insertion_converter = ImageInsertionConverter("./", "./")

    def test_find_md_files(self):
        md_files = self.image_insertion_converter.find_md_files("./")
        print(md_files)
        self.assertEqual(
            first=md_files,
            second=['./markdown_with_refs.md',
                    './markdown_with_tags.md',
                    './for_recursion_test\\test_dir\\inner_markdown.md']
        )

    def test_tag_to_ref(self):
        self.image_insertion_converter.tag_to_ref(['./markdown_with_tags.md'], False)

        with open('./markdown_with_tags_result.md', 'r', encoding='utf-8') as f:
            result_markdown  = f.read()

        with open('./markdown_with_refs.md', 'r', encoding='utf-8') as f:
            expected_markdown = f.read()

        self.assertEqual(result_markdown, expected_markdown)

        pass

    def test_ref_to_tag(self):
        pass


if __name__ == '__main__':
    unittest.main()
