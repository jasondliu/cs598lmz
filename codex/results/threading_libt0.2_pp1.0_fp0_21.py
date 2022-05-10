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
        self.max_level = -1

    def dfs(self, root, level):
        if root is None:
            return
        if level > self.max_level:
            self.ans = root.val
            self.max_level = level
        self.dfs(root.right, level + 1)
        self.dfs(root.left, level + 1)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.ans

def createTree(
