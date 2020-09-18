#!/usr/bin/env python


# 79. Word Search
# Medium

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def search(board, i, j, word):
            if len(word) == 0:
                return True

            if i >= m or i < 0 or j >= n or j < 0 or word[0] != board[i][j]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'

            res = search(board, i, j + 1, word[1:]) or search(board, i, j - 1, word[1:]) or search(board, i + 1, j, word[1:]) or search(board, i - 1, j, word[1:])
            board[i][j] = tmp
            return res
        for i in range(m):
            for j in range(n):
                if search(board,i,j, word):
                    return True
        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

A = Solution()
print(A.exist(board, 'ABCCED'))
print(A.exist(board, 'SEE'))
print(A.exist(board, 'ABCB'))
