from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for n in range(len(nums)):
        for i in range(len(nums) - 1 - n):
            if nums[n] + nums[n + i + 1] == target:
                return [n, n + i + 1]


def twoSum1(nums: List[int], target: int) -> List[int]:
    sums = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in sums:
            return [sums[diff], i]
        else:
            sums[num] = i
    return -1


if __name__ == '__main__':
    nums = [2, 5, 5, 11]
    target = 10
    a = twoSum(nums, target)
    print(a)
    print(twoSum1(nums, target))
