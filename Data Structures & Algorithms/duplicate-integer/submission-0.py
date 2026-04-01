class Solution:
    def hasDuplicate(self, nums):
        hashes = set()
        for num in nums:
            if num in hashes:
                return True
            hashes.add(num)
        return False