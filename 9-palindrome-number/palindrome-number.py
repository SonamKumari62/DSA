class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindrome
        if x < 0:
            return False

        temp = x
        rev = 0

        while temp > 0:
            rem = temp % 10
            rev = rev * 10 + rem
            temp //= 10

        return rev == x