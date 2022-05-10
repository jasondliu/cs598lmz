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
        def isValid(root, min, max):
            if root is None:
                return True
            if root.val <= min or root.val >= max:
                return False
            return isValid(root.left, min, root.val) and isValid(root.right, root.val, max)
        return isValid(root, float('-inf'), float('inf'))

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

   
