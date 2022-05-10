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
    def bstFromPreorder(self, A: List[int]) -> TreeNode:
        if len(A) == 0:
            return None
        root = TreeNode(A[0])
        stack = [root]
        for i in range(1, len(A)):
            temp = None
            while len(stack) > 0 and A[i] > stack[-1].val:
                temp = stack.pop()
            if temp:
                temp.right = TreeNode(A[i])
                stack.append(temp.right)
            else:
                temp = stack[-1]
                temp.left
