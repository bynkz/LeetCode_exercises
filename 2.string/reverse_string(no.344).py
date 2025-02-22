from typing import List


class Solution:

    # solution 1
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp_index: int
        tmp_letter: str
        for i in range(int(len(s)/2)):
            tmp_index = (i * (-1)) - 1
            tmp_letter = s[tmp_index]
            s[tmp_index] = s[i]
            s[i] = tmp_letter
        print(s)

    # solution 2
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j: int = len(s)
        for i in range(j):
            if i == j or j-i == 1:
                print(s)
                return
            else:
                tmp_letter: str = s[i]
                s[i] = s[j-1]
                s[j-1] = tmp_letter
                i += 1
                j -= 1
        

    # solution 3
    def reverseString3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  
        print(s)


new_sol = Solution()
new_sol.reverseString(s = ['h', 'e', 'l', 'l', 'o'])
new_sol.reverseString2(s = ['h', 'e', 'l', 'l', 'o'])
new_sol.reverseString3(s = ['h', 'e', 'l', 'l', 'o'])