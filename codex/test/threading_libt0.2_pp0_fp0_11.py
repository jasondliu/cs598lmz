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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        x_parent, y_parent = None, None
        x_depth, y_depth = 0, 0
        stack = [(root, None, 0)]
        while stack:
            node, parent, depth = stack.pop()
            if node.val == x:
                x_parent, x_depth = parent, depth
            if node.val == y:
                y_parent, y_depth = parent, depth
