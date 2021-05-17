import unittest
import wordCount


class wordCountTestCase(unittest.TestCase):
    def test_count(self):
        self.assertEqual(wordCount.wordCount("I love you"), 3)
        self.assertEqual(wordCount.wordCount("You are the most beautiful woman I've ever seen."), 9)
        self.assertEqual(wordCount.wordCount("Will you marry me"), 1)
