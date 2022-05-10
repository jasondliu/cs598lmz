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
        def dfs(root, curr):
            if not root:
                return
            curr = curr * 2 + root.val
            if not root.left and not root.right:
                self.ans += curr
            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root, 0)
        return self.ans

def createTree(list):
    if len(list) == 0:
       
