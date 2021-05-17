import unittest
import palindrome


class Test(unittest.TestCase):

    def test_true(self):
        self.assertEqual(palindrome.palindrome("racecar"), True)

    def test_false(self):
        self.assertEqual(palindrome.palindrome("beef"), False)


if __name__ == '__main__':
    unittest.main()
