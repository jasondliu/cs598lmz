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
        self.max_depth = 0

    def dfs(self, root, depth):
        if not root:
            return
        if depth > self.max_depth:
            self.max_depth = depth
            self.ans = root.val
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.dfs(root, 1)
        return self.ans

def createTree(data,
