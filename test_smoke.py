import unittest
from pathlib import Path


class TestSmoke(unittest.TestCase):
    def test_smoke_agy(self):
        smoke_file = Path(__file__).resolve().parent / "smoke" / "agy.txt"
        self.assertTrue(smoke_file.is_file(), f"{smoke_file} does not exist")
        self.assertEqual(smoke_file.read_text(encoding="utf-8"), "smoke-ok")

    def test_smoke_claude(self):
        smoke_file = Path(__file__).resolve().parent / "smoke" / "claude.txt"
        self.assertTrue(smoke_file.is_file(), f"{smoke_file} does not exist")
        self.assertEqual(smoke_file.read_text(encoding="utf-8"), "smoke-ok")

    def test_readme_purpose(self):
        readme = Path(__file__).resolve().parent / "README.md"
        self.assertTrue(readme.is_file(), f"{readme} does not exist")
        content = readme.read_text(encoding="utf-8")
        self.assertIn("## Purpose", content)
        self.assertIn("disposable", content)
        self.assertIn("throwaway", content)


if __name__ == "__main__":
    unittest.main()
