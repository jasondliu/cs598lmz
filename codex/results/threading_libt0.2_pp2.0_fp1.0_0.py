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

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, val):
        if not root:
            return
        val = val * 2 + root.val
        if not root.left and not root.right:
            self.ans += val
        self.dfs(root.left, val)
        self.dfs(root.right, val)

def createTree(list):
    if len(list) == 0:
