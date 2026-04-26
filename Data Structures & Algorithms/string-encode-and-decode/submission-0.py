class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            length = len(word)
            code += str(length) + "#" + word
        return code
    def decode(self, s: str) -> List[str]:
        bank = []
        i = 0 
        while i < len(s):
            j = s.index("#",i)
            print(j)
            length = int(s[i:j])
            i = j + 1 + length
            bank.append(s[j+1:i])
        return bank
            

        
