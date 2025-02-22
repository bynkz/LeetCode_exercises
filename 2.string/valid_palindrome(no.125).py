class Solution:

    # solution 1 (kinda cheat tho)
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        #cheat
        if len(s) <= 1:  
            return True  
        mid_index: int = len(s)//2
        s2: str = s[-mid_index:]
        return s[:mid_index] == s2[::-1]
    
    #solution 2
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        j: int = -1
        for i in range(len(s)//2):
            if s[j] != s[i]:
                return False
            j -= 1
        return True

def run_tests():
    test_cases = [
        ("A man, a plan, a canal: Panama"),    # Expected: true
        ("race a car"),         # Expected: false
        (" " ),            # Expected: true
        ("A" ),            # Expected: true
    ]

    new_sol = Solution()

    for es in test_cases:
        output1 = new_sol.isPalindrome(es)
        output2 = new_sol.isPalindrome2(es)
        print(f"Input: s={es}")
        print(f"Output (isPalindrome): {output1}")
        print(f"Output (isPalindrome2): {output2}")

run_tests()
