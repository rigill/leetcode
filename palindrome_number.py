# https://leetcode.com/problems/palindrome-number/
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

print(isPalindrome(121) == True)
