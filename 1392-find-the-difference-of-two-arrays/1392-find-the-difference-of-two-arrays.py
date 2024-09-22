class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set2 = set(nums2)
        set1 = set(nums1)
        n1 = [i for i in set1 if i not in set2]
        n2 = [i for i in set2 if i not in set1]
        return [ n1,n2]
