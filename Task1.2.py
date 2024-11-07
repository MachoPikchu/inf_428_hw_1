class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        length1=len(nums1)
        index=length1-1
        while n>0 and m>0:
            if nums2[n-1]>=nums1[m-1]:
                nums1[index]=nums2[n-1]
                n=n-1
            else:
                nums1[index]=nums1[m-1]
                m=m-1
            index=index-1
        
        while n>0:
            nums1[index]=nums2[n-1]
            n=n-1
            index=index-1
            
        