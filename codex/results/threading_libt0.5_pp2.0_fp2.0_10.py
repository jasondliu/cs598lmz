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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        self.s = 0
        
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.s += root.val
            root.val = self.s
            dfs(root.left)
        
        dfs(root)
        
        return root
