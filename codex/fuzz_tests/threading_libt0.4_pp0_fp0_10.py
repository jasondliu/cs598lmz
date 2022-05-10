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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

def createTree(data, i):
    if i >= len(data):
        return None
    else:
