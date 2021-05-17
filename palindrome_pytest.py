import pytest
import palindrome


def test_true():
    assert palindrome.palindrome("racecar") == True


def test_false():
    assert palindrome.palindrome("cheesecake") == False


