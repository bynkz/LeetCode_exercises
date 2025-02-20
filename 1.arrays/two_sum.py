from typing import List

# solution 1
# O(n^2)
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# solution 2
# O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dictmap = dict()
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in dictmap:
                return [dictmap[rest], i]
            else:
                dictmap[nums[i]] = i


def run_tests():
    test_cases = [
        ([2, 7, 11, 15], 9),    # Expected: [0, 1]
        ([3, 2, 4], 6),         # Expected: [1, 2]
        ([3, 3], 6),            # Expected: [0, 1]
    ]
    new_sol = Solution()
    for nums, target in test_cases:
        output1 = new_sol.twoSum(nums, target)
        output2 = new_sol.twoSum2(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output (twoSum): {output1}")
        print(f"Output (twoSum2): {output2}")


run_tests()