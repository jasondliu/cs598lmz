import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, curr, val):
        if curr.val < val:
            if curr.right is None:
                curr.right = TreeNode(val)
            else:
                self._insert(curr.right, val)
        else:
            if curr.left is None:
                curr.left = TreeNode(val)
            else:
                self._insert
