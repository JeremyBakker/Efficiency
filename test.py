import unittest
from learn import return_max_profit, binary_search, highest_product_of_three, \
is_unique, is_unique_without_addition, binary_gap, find_missing_element,\
integer_pairs, string_compression, check_permutation, isSubstring

class TestProblemSolving(unittest.TestCase):

    def test_return_max_profit(self):
        self.assertRaises(IndexError, return_max_profit, [])
        self.assertEqual(return_max_profit([10, 7, 5, 8, 11, 9]), 6)
        self.assertEqual(return_max_profit([10, 11, 12, 13, 14, 15]), 5)
        self.assertEqual(return_max_profit([15, 14, 12, 6, 11, 25]), 19)
        self.assertEqual(return_max_profit([15, 14, 12, 6, 5, 4]), 0)

    def test_binary_search(self):
        self.assertTrue(binary_search(8, [1,2,8,45,1203819283]))
        self.assertFalse(binary_search(1, [2,3,5,7,89,120]))

    def test_highest_product_of_three(self):
        self.assertEqual(highest_product_of_three([1, 5, 20, -1]), 100)
        self.assertEqual(highest_product_of_three([-1, 1, -50, -2]), 100)
        self.assertRaises(IndexError, highest_product_of_three, [1,2])

    def test_is_unique(self):
        self.assertRaises(ValueError, is_unique, '')
        self.assertEqual(is_unique("abcdefghijklmnop"), True)
        self.assertEqual(is_unique("aaabdflkjafna;lkj"), False)

    def test_is_unique_without_addition(self):
        self.assertEqual(is_unique("abcdefghijklmnop"), True)
        self.assertEqual(is_unique("aaabdflkjafna;lkj"), False)

    def test_binary_gap(self):
        self.assertEqual(binary_gap(1041), 5)
        self.assertEqual(binary_gap(20), 1)
        self.assertEqual(binary_gap(15), 0)

    def test_integer_pairs(self):
        self.assertEqual(integer_pairs([1,2,3,7,4,3,1,2]), 7)
        self.assertEqual(integer_pairs([2,2,3,3,7,7,8,4,3,3,5,6,4,5,6]), 8)

    def test_find_missing_element(self):
        self.assertEqual(find_missing_element([1,2,3,5]), 4)
        self.assertEqual(find_missing_element([1,2,3,4,5,6,7,8,9,11,12]), 10)

    def test_string_compression(self):
        self.assertEqual(string_compression('AABBBCAAAA'), 'A2B3C1A4')
        self.assertEqual(string_compression('abcdef'), 'abcdef')

    def test_check_permutation(self):
        self.assertEqual(check_permutation(['abba', 'baaa']), False)
        self.assertEqual(check_permutation(['abbacc', 'bccbaa']), True)

    def test_isSubstring(self):
        self.assertEqual(isSubstring("waterbottle", "erbottlewat"), True)
        self.assertEqual(isSubstring("dog", "cat"), False)
        self.assertEqual(isSubstring("dog", "god"), False)
        self.assertEqual(isSubstring("dog", "gdo"), True)


if __name__ == '__main__':
    unittest.main()