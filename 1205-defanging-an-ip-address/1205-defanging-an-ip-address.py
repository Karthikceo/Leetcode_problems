class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
           if i == ".":
               ans = ans + "[.]"
           else:
               ans = ans + i
        return ans 