#!/usr/bin/python3

class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i

        for j in range(0, len(nums)):
            temp = target - nums[j]
            if temp not in d:
                continue
            if (j == d[temp]):
                continue
            if temp in d:
                return [j, d[temp]]
        return []

s = Solution()
assert [0,1] == s.twoSum([2,7,11,15], 9)
assert [1,2] == s.twoSum([3,2,4], 6)
assert [0,1] == s.twoSum([3,3], 6)

print("1")
