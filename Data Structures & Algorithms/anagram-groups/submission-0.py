class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        library = {}
        final = []
        for str in strs:
            sorted_str = "".join(sorted(str)) 
            if sorted_str not in library:
                library[sorted_str] = []
                library[sorted_str].append(str)
            else:
                library[sorted_str].append(str)
        for key, value in library.items():
            final.append(value)
        return final



