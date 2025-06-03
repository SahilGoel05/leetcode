class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        after = dict.fromkeys(nums, False)
        before = dict.fromkeys(nums, False)
        max_len = 1

        for num in nums:
            if (num-1) in after:
                after[num-1] = True
            if (num+1) in before:
                before[num+1] = True

        for key, value in after.items():
            tmp_len = 1
            cur_val = key
            after_bool = value
            while after_bool == True:
                tmp_len += 1
                cur_val += 1
                after_bool = after[cur_val]
                after[cur_val] = False
                before[cur_val] = False

            cur_val = key
            before_bool = before[key]
            while before_bool == True:
                tmp_len += 1
                cur_val -= 1
                before_bool = before[cur_val]
                after[cur_val] = False
                before[cur_val] = False

            max_len = max(tmp_len, max_len)
            after[cur_val] = False
            before[cur_val] = False
        
        return max_len

'''
TC = O(n)
SC = O(n)

Optimal solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

TC = O(n)
SC = O(n)
'''

