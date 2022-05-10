import threading
threading.stack_size(2**27)
import sys
import math
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 and t2 and t1.val == t2.val:
            return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        return False


def createTree(data, tree, index, n):
    if index < n:
       
