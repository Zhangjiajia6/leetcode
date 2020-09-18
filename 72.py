# 72. Edit Distance
# Hard

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]


        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1

        return dp[-1][-1]

case1 = ('horse', 'ros')
case2 = ('intention', 'excution')

S = Solution()
res1 = S.minDistance(*case1)
print('res1:', res1)

res2 = S.minDistance(*case2)
print('res2:', res2)
