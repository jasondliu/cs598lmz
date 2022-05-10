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

def createTree(arr):
    n = len(arr)
    if n == 0:
        return None
    root = TreeNode(arr[0])
    def helper(i, root):
        if 2*i+1 < n and arr[2*i+1] is not None:
            root.left = TreeNode(arr[2*i+1])
            helper(2*i+1, root.left)
        if 2*i+2 < n and arr[2*i+2] is not None:
            root.right = TreeNode(arr[2*i+2])
            helper(2*i+2, root.
