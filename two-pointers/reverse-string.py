class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        d =[]
        x=len(s)
        for i in range (x):
            d.append(s[x-1-i])
        for j in range (x):
            s[j]=d[j]


        