class Solution:
    '''
    nums: [1,2,4,6]

    i=
    prev_product = 6
    larr: [1, 1, 2, 8]
    rarr: [48,24,6, 1]
    farr: []
    '''

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [1]
        rarr = [1] * (len(nums))
        farr = []
        prev_product = 1
        for i in range(len(nums) - 1):
            tmp = nums[i] * prev_product
            larr.append(tmp)
            prev_product = tmp
        prev_product = 1
        for i in range(len(nums) - 1, 0, -1):
            tmp = nums[i] * prev_product
            rarr[i - 1] = tmp
            prev_product = tmp
        for i in range(len(nums)):
            farr.append(larr[i] * rarr[i])

        return farr
        

'''
TC: O(n)
SC: O(n)

Optimal solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

TC: O(n)
SC: O(1) extra space, O(n) for the output array
'''
