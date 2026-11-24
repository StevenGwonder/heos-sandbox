import unittest

from sandbox_math import add, clamp


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

    def test_clamp_below_range(self):
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_clamp_inside_range(self):
        self.assertEqual(clamp(4, 0, 10), 4)

    def test_clamp_above_range(self):
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_clamp_bounds(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)
        self.assertEqual(clamp(5, 5, 5), 5)

    def test_clamp_invalid_bounds(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
