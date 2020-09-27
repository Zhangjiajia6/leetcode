# 200. Number of Islands
# Medium

from typing import List


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

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
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1

        self.count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def cord2index(i, j):
            return i * col + j

        try:
            row, col = len(grid), len(grid[0])
        except IndexError:
            return 0
        S = UnionFind(row * col + 1)
        dummy_node = row * col
        directions = [(1, 0), (0, 1)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    S.union(cord2index(i, j), dummy_node)
                else:
                    for d in directions:
                        x = i + d[0]
                        y = j + d[1]
                        if x < row and y < col and grid[x][y] == '1':
                            S.union(cord2index(i, j), cord2index(x, y))

        return S.count - 1


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)
