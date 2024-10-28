from typing import List
'''
I believe this solution is trying to use a 2 pointer style solution.
looping through nums, pointing to indexed value to be replaced and indexed value to compare
'''
class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        index = 0
        nums2 = []
        for i in range(len(nums)):
            if nums[i] != val: # iterator 'i' is the pointer looking through each value in nums
                nums[index] = nums[i]  # points to value to be replaced with valid value
                index += 1  # moves to next point in nums to be replaced
                nums2.append(nums[i])  # to display what's happening in nums live
                print('nums2', nums2)
        return nums2  # nums actually should be nums not nums2 
sol = Solution()

print(sol.remove_element([0,1,2,2,3,0,4,2], 2))
print('RESULT', sol.remove_element([3,2,2,3], 3))


