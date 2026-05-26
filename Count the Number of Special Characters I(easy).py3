class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)

        count = 0

        for i in range(26):
            ch = chr(ord('a') + i)
            if ch in lower and ch.upper() in upper:
                count += 1

        return count   
