class Solution:
    def findMin(self, nums: List[int]) -> int:
        c = len(nums) // 2
        r = len(nums) - 1

        if c != r:
            if nums[c] < nums[r]:
                return self.findMin(nums[:c+1])
            elif nums[c] > nums[r]:
                return self.findMin(nums[c+1:])

        return min(nums[c], nums[c-1])

'''
TC: O(logn)
SC: O(n) <- Unoptimal

Optimal solution:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

TC: O(logn)
SC: O(1) <- Due to use of indices rather than recursion
'''
