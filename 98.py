# 98. Validate Binary Search Tree
# Medium


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, llimit=float('-inf'), rlimit=float('inf')):
            if not node:
                return True
            if node.val <= llimit or node.val >= rlimit:
                return False
            return helper(node.left, llimit, node.val) and helper(node.right, node.val, rlimit)
        return helper(root)
