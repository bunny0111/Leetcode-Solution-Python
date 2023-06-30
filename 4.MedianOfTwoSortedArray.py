'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        output_list = []
        while(nums1 and nums2):
            if nums1[0] <= nums2[0]:
                output_list.append(nums1.pop(0))
            else:
                output_list.append(nums2.pop(0))
        while nums1:
            output_list.append(nums1.pop(0))
        while nums2:
            output_list.append(nums2.pop(0))
        mid = len(output_list) // 2
        if len(output_list) % 2 != 0:
            return(output_list[mid])
        return(float(output_list[mid] + output_list[mid - 1])/2)