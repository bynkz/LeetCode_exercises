from typing import List
from copy import deepcopy

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxed :List[int] = [0] *len(nums)
        if nums == []:
            return 0
        elif len(nums) == 1:
            return nums[0]
        maxed[0] = nums[0]
        maxed[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxed[i] = max(maxed[i-2] + nums[i], maxed[i-1])
        print(maxed[i])
        return maxed[-1]




new_sol = Solution()
new_sol.rob([2,1,2])
new_sol.rob([1,2,3,1])
new_sol.rob([2,7,9,3,1])
new_sol.rob([6,1,2,9,2])
