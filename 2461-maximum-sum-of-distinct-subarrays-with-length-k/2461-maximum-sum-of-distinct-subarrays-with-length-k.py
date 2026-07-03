class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        left = 0
        window_elements = set()
        
        for right in range(len(nums)):
            # If a duplicate is found, shrink the window from the left 
            # until the duplicate element is removed
            while nums[right] in window_elements:
                window_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
                
            # Add the current element to the window
            window_elements.add(nums[right])
            current_sum += nums[right]
            
            # If the window size exceeds k, remove the leftmost element
            if right - left + 1 > k:
                window_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
                
            # If the window is exactly size k, update our maximum sum
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                
        return max_sum
