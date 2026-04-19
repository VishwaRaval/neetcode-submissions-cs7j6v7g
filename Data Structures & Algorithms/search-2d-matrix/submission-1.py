class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nums = []
        for row in matrix:
            nums.extend(row)

        l, r = 0, len(nums) - 1

        while l<=r:
            m = (l+r)//2
            if target>nums[m]:
                l = m+1
            elif target<nums[m]:
                r = m-1
            else:
                return True
        return False

        