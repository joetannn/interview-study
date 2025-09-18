
# https://leetcode.com/problems/two-sum/description



class Solution:
    # inefficient solution: O(n^2)
    # this solution is O(n^2)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
    # more efficient solution
    # this solution is O(n) as it goes through in one pass, where n is the number of elements
    def twoSum2(self, nums, target):
        numDict = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in numDict:
                numDict[target - curr] = i
            else:
                return [i, numDict[curr]]

                
        
