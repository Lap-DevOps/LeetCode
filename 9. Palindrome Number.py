def isPalindrome(x: int) -> bool:
    return False if x < 0 else str(x)[::-1] == str(x)


if __name__ == '__main__':
    print(isPalindrome(1211))
