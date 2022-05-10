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

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
    
    def _insert(self, curr, val):
        if val < curr.val:
            if curr.left == None:
                curr.left = TreeNode(val)
            else:
                self._insert(curr.left, val)
        else:
            if curr.right == None:
                curr.right =
