import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        inorder = sorted(preorder)
        return self.bstFromPreorderInorder(inorder, preorder)

    def bstFromPreorderInorder(self, inorder, preorder) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.bstFromPreorderInorder(inorder[0:ind], preorder)
            root.right = self.bstFromPreorderInorder(inorder
