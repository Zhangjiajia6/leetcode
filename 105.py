# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        queue = deque(preorder)
        d = {val: i for i,val in enumerate(inorder)}

        def helper(preorder, start, end):
            if start < end:
                idx = d[preorder.popleft()]
                root = TreeNode(inorder[idx])
                root.left = helper(preorder, start, idx)
                root.right = helper(preorder, idx+1, end)
                return root
        return helper(queue, 0, len(inorder))


