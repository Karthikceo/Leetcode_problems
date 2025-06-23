class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in range(len(sentences)):
            ch = sentences[i]
            temp = 1
            for j in range(len(ch)):
                s = ch[j]
                if s == " ":
                    temp = temp+1
            ans = max(ans , temp)
        return ans