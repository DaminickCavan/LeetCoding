from typing import List

"""
THIS IS A 2 POINTER/ARRAY EXAMPLE!!!!
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #m for number of elements in nums1 and n for nums 2
        print('NUMS 1 INITIAL VALUE', nums1)
        print('NUMS 2 INITIAL VALUE', nums2)

        if n == 0: return nums1 # if 
        nums1_end_indx = len(nums1)-1  # getting the ending indx to point to end of nums1 list (moving from right to left)
        while n > 0 and m > 0:  # continue until both n and m are empty'
            print('VALUE TO BE REPLACED', nums1[nums1_end_indx]) # this is the value that nums1_end_indx is pointing to in nums1 list that is going to be replaced
            print('M:',m, 'N:', n)
            if nums2[n-1] >= nums1[m-1]:
                nums1[nums1_end_indx] = nums2[n-1] 
                print('NEW VALUE', nums2[n-1])
                n-=1 # move nums2 pointer
                
            else:
                nums1[nums1_end_indx] = nums1[m-1]
                print('NEW VALUE', nums1[m-1])
                m-=1 # move nums1 pointer
            print('UPDATED LIST', nums1) # see how the pointer is moving across?
            nums1_end_indx-=1 # points to indexed value to be replaced

        while n > 0:
            print('VALUE TO BE REPLACED', nums1[nums1_end_indx])
            nums1[nums1_end_indx] = nums2[n-1]
            print('NEW VALUE', nums2[n-1])
            n-=1
            nums1_end_indx-=1
            print(nums1)
        return nums1

sol = Solution()
print('CASE 1 -------------- RESULT', sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print('CASE 2 -------------- RESULT', sol.merge([1], 1, [], 0))
print('CASE 3 -------------- RESULT', sol.merge([0], 0, [1], 1))