import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return -float('inf')
            l = dfs(node.left)
            r = dfs(node.right)
            ans = node.val + max(l, r, 0)
            self.ans = max(self.ans, ans, node.val + l + r)
            return ans

        dfs(root)
        return self.ans



def createTree(l):
    root = TreeNode(
