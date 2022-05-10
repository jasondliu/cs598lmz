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
        self.ans = True
        self.prev = -math.inf
        self.inorder(root)
        return self.ans

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev >= root.val:
            self.ans = False
        self.prev = root.val
        self.inorder(root.right)

def createTree(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[
