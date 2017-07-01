import unittest
from learn import return_max_profit, reduce_without_index

class TestProblemSolving(unittest.TestCase):

    def test_return_max_profit(self):
        self.assertRaises(IndexError, return_max_profit, [])
        self.assertEqual(return_max_profit([10, 7, 5, 8, 11, 9]), 6)
        self.assertEqual(return_max_profit([10, 11, 12, 13, 14, 15]), 5)
        self.assertEqual(return_max_profit([15, 14, 12, 6, 11, 25]), 19)
        self.assertEqual(return_max_profit([15, 14, 12, 6, 5, 4]), 0)

    # def test_reduce_without_index(self):
        # self.assertEqual(reduce_without_index([1,7,3,4]), [84,12,28,21])

if __name__ == '__main__':
    unittest.main()