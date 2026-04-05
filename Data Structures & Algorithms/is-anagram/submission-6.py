class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        data = {}

        for letter in s:
            data[letter] = data.get(letter, 0) + 1

        for letter in t:
            if letter not in data:
                return False
            data[letter] -= 1
            if data[letter] < 0:
                return False

        return True