class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        start = 0
        
        for end, num in enumerate(nums):
            if num == 0:
                start = end + 1
            else:
                max_length = max(max_length, end - start + 1)
                
        return max_length
