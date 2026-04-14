from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bank = {}

        for num in nums:
            if num not in bank:
                bank[num] = 1
            else:
                bank[num] += 1

        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        for key, value in bank.items():
            bucket[value].append(key)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result