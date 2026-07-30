from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Loop 1: Calculate the sum of the first window
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
            
        # Set max_sum ONLY AFTER the full first window is computed
        max_sum = window_sum
        
        # Loop 2: Slide the window from index k to len(nums)
        for j in range(k, len(nums)):
            # Add the new element (nums[j]), remove the old element (nums[j - k])
            window_sum += nums[j] - nums[j - k]
            
            if window_sum > max_sum:
                max_sum = window_sum
                
        return max_sum / k