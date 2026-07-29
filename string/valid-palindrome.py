class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=len(s)
        left,right =0,x-1
        for i in range x:
            while left<right:
                if s[left]!=s[right]:
                    return False
                return True
