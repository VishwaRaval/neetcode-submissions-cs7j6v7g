class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # left, append
            subset.append(nums[i])
            dfs(i+1)

            #right, dont append
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
            

