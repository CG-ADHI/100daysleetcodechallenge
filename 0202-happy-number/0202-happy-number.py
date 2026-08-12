class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()

        while n != 1 and n not in seen_nums:
            seen_nums.add(n)
            sqsum = 0

            while n > 0:
                ld = n % 10
                sqsum = sqsum + ld ** 2
                n = n // 10

            n = sqsum

        if n == 1:
            return True
        else:
            return False