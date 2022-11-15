import unittest
import QuickSelect as qs

class TestQuickSelect(unittest.TestCase):

    def test_partition(self):
        pass

    def test_QuickSelect_singleton(self):
        self.assertEqual(qs.quickSelect([0], 1), 0)

    def test_QuickSelect_large_set(self):
        self.assertEqual(qs.quickSelect([75, 65, 3, 86, 24, 72, 19, 89, 98, 40, 17, 26, 82, 93, 28, 57, 4, 90, 80, 55, 37, 20, 88, 29, 41, 54, 64, 38, 51, 49, 2, 13, 14, 70, 58, 34, 48, 97, 47, 99, 79, 44, 21, 73, 100, 33, 7, 11, 32, 36], 100), 100)
    
    def test_QuickSelect_in_order(self):
        self.assertEqual(qs.quickSelect([2, 4, 6, 8, 10], 3), 6)

    def test_QuickSelect_post_order(self):
        self.assertEqual(qs.quickSelect([10, 8, 6, 4, 2], 3), 6)

    def test_QuickSelect_at_front(self):
        self.assertEqual(qs.quickSelect([6, 4, 2, 8, 10], 3), 6)

    def test_QuickSelect_at_end(self):
        self.assertEqual(qs.quickSelect([2, 4, 10, 8, 6], 3), 6)

    def test_QuickSelect_find_largest(self):
        self.assertEqual(qs.quickSelect([18, 5, 3, 11, 13], 5), 18)

    def test_QuickSelect_find_smallest(self):
        self.assertEqual(qs.quickSelect([16, 9, 8, 14, 15], 1), 8)

    def test_QuickSelect_general_1(self):
        self.assertEqual(qs.quickSelect([17, 9, 4, 2, 16], 3), 9)

    def test_QuickSelect_general_2(self):
        self.assertEqual(qs.quickSelect([14, 10, 19, 2, 8], 3), 10)

    def test_QuickSelect_general_3(self):
        self.assertEqual(qs.quickSelect([16, 5, 2, 9, 13], 3), 9)

    def test_QuickSelect_general_4(self):
        self.assertEqual(qs.quickSelect([5, 11, 6, 19, 2], 3), 6)

    def test_QuickSelect_general_5(self):
        self.assertEqual(qs.quickSelect([18, 4, 7, 15, 19], 3), 15)

    def test_QuickSelect_general_6(self):
        self.assertEqual(qs.quickSelect([18, 17, 13, 6, 16], 3), 16)