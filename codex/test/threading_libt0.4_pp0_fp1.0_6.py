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
        if root is None:
            return True
        if root.left is not None and root.val <= root.left.val:
            return False
        if root.right is not None and root.val >= root.right.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

def createTree(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    i = 0
