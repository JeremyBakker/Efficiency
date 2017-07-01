import unittest
from learn import return_max_profit

class TestProblemSolving(unittest.TestCase):

    def test_return_max_profit(self):
        self.assertEqual(return_max_profit([10, 7, 5, 8, 11, 9]), 6)
        self.assertEqual(return_max_profit([10, 11, 12, 13, 14, 15]), 5)
        self.assertEqual(return_max_profit([15, 14, 12, 6, 11, 25]), 19)
        self.assertEqual(return_max_profit([15, 14, 12, 6, 5, 4]), 0)

if __name__ == '__main__':
    unittest.main()