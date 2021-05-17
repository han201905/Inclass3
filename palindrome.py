def palindrome(string):
    str = string[::-1]
    if str == string:
        return 1
    else:
        return 0
