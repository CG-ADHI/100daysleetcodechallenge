class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlen = 0

        for n in numSet:

            if n - 1 not in numSet:

                curnum = n ; curmaxlen = 1

                while curnum + 1 in numSet:
                    curnum += 1
                    curmaxlen = curmaxlen + 1

                maxlen = max(maxlen, curmaxlen)

        return maxlen