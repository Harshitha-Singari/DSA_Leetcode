class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        sum = 0
        maxAvg = float("-inf")
        while end < len(nums):
            sum += nums[end]
            if end - start +1 < k:
                end+=1
            else:
                avg=sum/k
                maxAvg = max(maxAvg,avg)
                sum -= nums[start]
                start+=1
                end+=1
        return maxAvg