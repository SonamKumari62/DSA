class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        digit_sum = 0
        product = 1

        while temp > 0:
            rem = temp % 10
            temp //= 10

            digit_sum += rem
            product *= rem

        return product - digit_sum