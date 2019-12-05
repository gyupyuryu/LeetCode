# Math
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        hold = x
        x = abs(x)
        # method of popping and pushing digits in reversing
        while x != 0:
            pop = x % 10
            x //= 10
            # floating point vs floor division
            rev = rev * 10 + pop
        if hold < 0:
            rev = -rev
        #print(rev)
        if rev >= 2 ** 31 - 1 or rev <= -2 ** 31:
            # Python is unbounded
            return 0
        else:
            return rev

x = -123
sol = Solution()
sol.reverse(x)

"""
hold1 = x
        x = abs(x)
        numlist = [int(x) for x in str(x)]
        revlist = []
        j = 0

        for i in range(len(numlist)):
            #print(numlist[i])
            revlist = [numlist[i]] + revlist
        for i in range(len(revlist)):
           if revlist[i] != 0:
                break
        else:
                j = j + 1

        revlist = revlist[j:len(revlist)]
        revlist2 = [str(x) for x in revlist]
        revlist3 = int("".join(revlist2))
        if hold1 < 0:
            revlist3 = -revlist3
        print(revlist3)
        return revlist3
        """
