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
    def buildTree(self, preorder, inorder):
        return self.helper(0, 0, len(inorder)-1, preorder, inorder)
    
    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inIndex = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == root.val:
                inIndex = i
        root.left = self
