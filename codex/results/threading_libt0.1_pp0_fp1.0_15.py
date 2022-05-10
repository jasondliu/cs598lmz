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
        self.n = 0
        self.arr = []
        self.tree = None

    def createTree(self, i):
        if i >= self.n:
            return None
        root = TreeNode(self.arr[i])
        root.left = self.createTree(2 * i + 1)
        root.right = self.createTree(2 * i + 2)
        return root

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right =
