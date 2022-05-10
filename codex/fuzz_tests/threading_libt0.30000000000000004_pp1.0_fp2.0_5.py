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
        def is_valid(root, min_val, max_val):
            if root is None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return is_valid(root.left, min_val, root.val) and is_valid(root.right, root.val, max_val)
        return is_valid(root, -sys.maxsize, sys.maxsize)

def createTree(list):
    if len(list) == 0:
        return None

