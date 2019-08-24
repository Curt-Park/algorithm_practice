"""
https://leetcode.com/problems/subsets/

78. Subsets
Medium

Given a set of distinct integers, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """O(N*2^N) / O(2^N)"""
        ret = []
        for i in range(2 ** len(nums)):
            subset = set()
            for j in range(len(nums)):
                if i & (1 << j):
                    subset.add(nums[j])
            ret.append(subset)
        return ret
