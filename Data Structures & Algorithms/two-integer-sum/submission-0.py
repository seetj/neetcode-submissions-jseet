class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = {}
        for index,num in enumerate(nums):
            difference = target - num
            if bank.get(difference) != None:
                return sorted([index,bank.get(difference)])
            bank[num]  = index


