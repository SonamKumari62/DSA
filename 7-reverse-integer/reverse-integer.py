class Solution:
    def reverse(self, x: int) -> int:

        sign = 1

        if x < 0:
            sign = -1

        temp = abs(x)
        rev = 0

        while temp > 0:
            rem = temp % 10
            temp //= 10
            rev = rev * 10 + rem

        rev = rev * sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev