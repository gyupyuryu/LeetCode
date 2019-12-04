class Solution:
    def findMedianSortedArrays(self, nums1: int, nums2: int) -> float:
        numstot = nums1+nums2
        numstot.sort()
        print(numstot)
        numslen = len(numstot)
        if numslen%2 !=0:
            mid = int(((numslen + 1) / 2) - 1)
            print(numstot[mid])
            median = numstot[mid]
            return median
        else:
            mid = int(((numslen) / 2) - 1)
            median = (numstot[mid]+numstot[mid+1])/2
            print(median)
            return median
        #if len1+len2 %2 == 0:
       #print(nums1[1])
x1 = [1, 2]
x2 = [3, 4]
p4 = Solution()
p4.findMedianSortedArrays(x1,x2)