# 139. Word Break
# Medium


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        WordDict = set(wordDict)

        for i in range(n):
            for j in range(i+1, n+1):
                if (not dp[j] and dp[i] and s[i:j] in WordDict):
                    dp[j] = True
        return dp[-1]
