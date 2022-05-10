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
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(root, min_val, max_val):
            if root is None:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            return validate(root.left, min_val, root.val) and validate(root.right, root.val, max_val)
        return validate(root, -float('inf'), float('inf'))
