import pytest
import wordCount

def test_1():
    text = "I love you"
    len = wordCount.wordCount(text)
    assert len == 3


def test_2():
    text = "You are the most beautiful woman I've ever seen."
    len = wordCount.wordCount(text)
    assert len == 9


def test_3():
    text = "Will you marry me"
    len = wordCount.wordCount(text)
    assert len == 1
