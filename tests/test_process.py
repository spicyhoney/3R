import unittest

from my_backend.process import total_count


class TotalCountTests(unittest.TestCase):
    def test_sums_counts(self):
        self.assertEqual(total_count([2, 3, 5]), 10)

    def test_empty_input(self):
        self.assertEqual(total_count([]), 0)
