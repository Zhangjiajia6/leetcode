# 96. Unique Binary Search Trees
# Medium

class Solution:
    def numTrees(self, n: int) -> int:
        res = [0 for _ in range(n+1)]
        res[0] = res[1] = 1
        if n <= 1:
            return 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                res[i] += res[j - 1] * res[i-j]
        return res[n]


S = Solution()
case1 = 3
res1 = S.numTrees(case1)
print(res1)
