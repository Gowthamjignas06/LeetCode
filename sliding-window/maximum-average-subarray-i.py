class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left,right=0,3
        sum,max=0,0
        for i in range (k):
            sum= sum+nums[i]
        max=sum
        for j in range(k,len(nums)):
            sum = sum-(nums[left])+(nums[right+1])
            left+=1
            right+=1
            if sum>max:
                max=sum
        return max/k