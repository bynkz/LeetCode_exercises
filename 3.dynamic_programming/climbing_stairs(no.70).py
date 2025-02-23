class Solution:

    # solution 1 : its right, but exceeds time limit
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return Solution.climbStairs(self, n-1) + Solution.climbStairs(self, n-2)

    # solution 2
    def climbStairs2(self, n: int) -> int:
        memory_dict = dict()
        memory_dict[1] = 1
        memory_dict[2] = 2
        for i in range(3, n +1 ):
            memory_dict[i] = memory_dict[i-1] + memory_dict[i-2]
        return memory_dict[n]




new_sol = Solution()
print(new_sol.climbStairs(n = 1))
print(new_sol.climbStairs(n = 5))
print(new_sol.climbStairs2(n = 1))
print(new_sol.climbStairs2(n = 5))
print(new_sol.climbStairs2(n = 44))

