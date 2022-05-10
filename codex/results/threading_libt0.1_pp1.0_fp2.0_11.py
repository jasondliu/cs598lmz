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
        def helper(root, min, max):
            if root is None:
                return True
            if root.val <= min or root.val >= max:
                return False
            return helper(root.left, min, root.val) and helper(root.right, root.val, max)
        return helper(root, -math.inf, math.inf)

def createTree(list):
    root = TreeNode(list[0])
    q = [root]
    i = 1
    while i < len(list):
        node = q
