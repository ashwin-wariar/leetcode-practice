def isPalindrome(x: int) -> bool:
    s = str(x)
    if s == s[::-1]: # [::-1] reverses the contents of a string, so we can check that with the original str version of the int
        return True
    else:
        return False