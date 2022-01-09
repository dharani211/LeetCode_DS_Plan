class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=-float('inf')
        Sum=0
        for i in range(0,len(nums)):
            Sum+=nums[i]
            if curr<Sum:
                curr=Sum
            if Sum<0:
                Sum=0
        return curr
