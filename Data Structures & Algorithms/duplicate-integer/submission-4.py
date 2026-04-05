class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bank = set()
        for num in nums:
            if num not in bank:
                bank.add(num)
            else:
                return True

        return False
