import unittest
import Counting_Inversions as ci

class TestCountingInversions(unittest.TestCase):

    def test_no_inversions(self):
        self.assertEqual(ci.countInversions([1, 2, 3], 0, 2)[0], 0)

    def test_all_inversions(self):
        self.assertEqual(ci.countInversions([3, 2, 1], 0, 2)[0], 3)

    def test_mixed(self):
        self.assertEqual(ci.countInversions([1, 1, 2, 1, 2, 1, 2, 1, 2, 2], 0, 9)[0], 6)