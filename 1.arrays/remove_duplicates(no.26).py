from typing import List

class Solution:

   # solution 1 
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = None
        uniqs = 0
        for i in range(len(nums)):
            if curr != nums[i]:
                curr = nums[i]
                nums[uniqs] = curr
                uniqs += 1
        return uniqs

def run_tests():
    test_cases = [
        ([1,1,2]),                  # 2, nums = [1,2,_]
        ([0,0,1,1,1,2,2,3,3,4])     # Expected: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    ]
    new_sol = Solution()
    for nums in test_cases:
        print(f"Input: nums={nums}")
        output1 = new_sol.removeDuplicates(nums)
        print(f"Output (removeDuplicates): {output1}, nums={nums}")
        print() 


run_tests()