class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sentence in sentences:
            temp = sentence.count(" ") + 1  
            ans = max(ans, temp)
        return ans