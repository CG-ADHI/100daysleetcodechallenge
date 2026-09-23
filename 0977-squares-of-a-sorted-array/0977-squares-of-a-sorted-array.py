class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        l = 0
        r = len(nums)-1
        while l<=r:
            left = nums[l]**2
            right = nums[r]**2
            if left < right:
                res.append(right)
                r -= 1
            else :
                res.append(left)
                l += 1
        return res[::-1]
