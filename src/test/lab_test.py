import unittest
from src.main.lab import *


class TestRangeFunctions(unittest.TestCase):
    def test_range_with_stop(self):
        stop = 5
        self.assertEqual(range_with_stop(stop), [0, 1, 2, 3, 4])

    def test_range_with_start_stop(self):
        start = 2
        stop = 7
        self.assertEqual(range_with_start_stop(start, stop), [2, 3, 4, 5, 6])

    def test_range_with_start_stop_step(self):
        start = 1
        stop = 10
        step = 2
        self.assertEqual(range_with_start_stop_step(start, stop, step), [1, 3, 5, 7, 9])


if __name__ == "__main__":
    unittest.main()
