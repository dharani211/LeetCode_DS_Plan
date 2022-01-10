class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        records = {nums[i]:i for i in range(n)}
        for i in range(n):
            add = records.get(target-nums[i])
            if add and add != i:
                return [i, add]
        
