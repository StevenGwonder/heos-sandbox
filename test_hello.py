import unittest
from pathlib import Path


class TestHello(unittest.TestCase):
    def test_hello(self):
        hello_file = Path(__file__).resolve().parent / "smoke" / "hello.txt"
        self.assertTrue(hello_file.is_file(), f"{hello_file} does not exist")
        self.assertEqual(hello_file.read_text(encoding="utf-8"), "hello from HEOS")


if __name__ == "__main__":
    unittest.main()
