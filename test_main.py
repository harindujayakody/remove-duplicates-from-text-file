import os
import tempfile
import unittest
from main import remove_duplicates, parse_args

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_remove_duplicates_sorted(self):
        in_path = os.path.join(self.test_dir.name, "in.txt")
        out_path = os.path.join(self.test_dir.name, "out.txt")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write("banana\napple\nbanana\ncherry\napple\n")

        dup_count, uniq_count = remove_duplicates(in_path, out_path, sort_lines=True)
        self.assertEqual(dup_count, 2)
        self.assertEqual(uniq_count, 3)

        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read().splitlines()

        self.assertEqual(content, ["apple", "banana", "cherry"])

    def test_remove_duplicates_keep_order(self):
        in_path = os.path.join(self.test_dir.name, "in.txt")
        out_path = os.path.join(self.test_dir.name, "out.txt")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write("banana\napple\nbanana\ncherry\napple\n")

        dup_count, uniq_count = remove_duplicates(in_path, out_path, sort_lines=False)
        self.assertEqual(dup_count, 2)
        self.assertEqual(uniq_count, 3)

        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read().splitlines()

        self.assertEqual(content, ["banana", "apple", "cherry"])

    def test_missing_file_raises_filenotfound(self):
        missing_path = os.path.join(self.test_dir.name, "nonexistent.txt")
        out_path = os.path.join(self.test_dir.name, "out.txt")

        with self.assertRaises(FileNotFoundError):
            remove_duplicates(missing_path, out_path)

    def test_unicode_content(self):
        in_path = os.path.join(self.test_dir.name, "in_unicode.txt")
        out_path = os.path.join(self.test_dir.name, "out_unicode.txt")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write("හෙලෝ\nworld\nහෙලෝ\n🌟\n🌟\n")

        dup_count, uniq_count = remove_duplicates(in_path, out_path, sort_lines=False)
        self.assertEqual(dup_count, 2)
        self.assertEqual(uniq_count, 3)

        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read().splitlines()

        self.assertEqual(content, ["හෙලෝ", "world", "🌟"])

    def test_parse_args_defaults(self):
        args = parse_args([])
        self.assertEqual(args.input_file, "input.txt")
        self.assertEqual(args.output_file, "new.txt")
        self.assertTrue(args.sort_lines)
        self.assertTrue(args.clear_screen)
        self.assertEqual(args.encoding, "utf-8")

    def test_parse_args_custom(self):
        args = parse_args(["-i", "source.txt", "-o", "target.txt", "--keep-order", "--no-clear"])
        self.assertEqual(args.input_file, "source.txt")
        self.assertEqual(args.output_file, "target.txt")
        self.assertFalse(args.sort_lines)
        self.assertFalse(args.clear_screen)

if __name__ == '__main__':
    unittest.main()
