"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lstr = ""
        length = len(s)+1
        for j in range(length):
            for i, value in enumerate(s):
                # print(s[j:i+1])
                s1 = s[j:i+1]
                # print(list(enumerate(s)))
                # print(s1[::-1])
                s2 = s1[::-1]
                if s1 == s2:
                    if len(s1) > len(lstr):
                        lstr = s1
                        print(type(lstr))

        print(lstr)
        return lstr
        """

class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
       # print(range(len(s), 1, -1))
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    #print(s[i:j])
                    print(s[0:5][::-1])
                    m = s[i:j]
                    break
        return m
x = "babad"
sol = Solution()
sol.longestPalindrome(x)
