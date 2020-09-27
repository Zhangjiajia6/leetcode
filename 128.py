# 128. Longest Consecutive Sequence
# Hard
from typing import List


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        self.set_size = [1]*n
    def find(self, p):
        if self.parent[p] == p:
            return p
        root = self.find(self.parent[p])
        self.parent[p] = root
        return root

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
            self.set_size[q_root] += self.set_size[p_root]
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
            self.set_size[p_root] += self.set_size[q_root]
        else:
            self.parent[p_root] = q_root
            self.set_size[q_root] += self.set_size[p_root]
            self.rank[q_root] += 1
        self.count -= 1


    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        uf = UnionFind(len(nums))
        d = {v:i for i,v in enumerate(nums)}
        for i,v in enumerate(nums):
            if v-1 in d:
                uf.union(i, d[v-1])
        return max(uf.set_size)


if __name__ == '__main__':
    solution = Solution()
    a = [100, 4, 200, 1, 3, 2]
    result = solution.longestConsecutive(a)
    print(result)
    a = [0]
    result = solution.longestConsecutive(a)
    print(result)
    a = [0,0,-1]
    result = solution.longestConsecutive(a)
    print(result)
    a = [1,2,0,1]
    result = solution.longestConsecutive(a)
    print(result)
    a = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    result = solution.longestConsecutive(a)
    print(result)