class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
        for letter in t:
            if letter not in dict or dict[letter] <= 0:
                return False
            else:
                dict[letter] -= 1

        return True