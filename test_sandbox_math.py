import unittest

from sandbox_math import add


class TestSandboxMath(unittest.TestCase):
    def test_add_ints(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 7), 7)

    def test_add_negatives(self):
        self.assertEqual(add(-4, -6), -10)
        self.assertEqual(add(-4, 9), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add(-1.5, 2.25), 0.75)


if __name__ == "__main__":
    unittest.main()
