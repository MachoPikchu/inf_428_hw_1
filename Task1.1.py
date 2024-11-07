class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        current_length=1
        max_length=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current_length+=1
                max_length=max(max_length,current_length)
            else:
                current_length=1

        return max_length
