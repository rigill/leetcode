# https://leetcode.com/problems/two-sum/
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash = {}
    for i, x in enumerate(nums):
        hash.update({x:i})

    for i, x in enumerate(nums):
        value = target - x
        if value in hash and hash[value] != i:
            return [i, hash[value]]


print(twoSum([3, 2, 3], 6) == [0, 2])
print(twoSum([2, 7, 11, 15], 9) == [0,1])
print(twoSum([3,2,4], 6))
print(twoSum([3,2,4], 6) == [1,2])
