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
    def isValidBST(self, root):
        self.prev = None
        return self.isMonotonicIncreasing(root)

    def isMonotonicIncreasing(self, root):
        if not root:
            return True
        if not self.isMonotonicIncreasing(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.isMonotonicIncreasing(root.right)

def stringToTreeNode(input):
    input = input.strip()
