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
    def isValidSequence(self, root, arr):
        return self.dfs(root, arr, 0)

    def dfs(self, root, arr, i):
        if root is None:
            return False
        if i == len(arr) - 1:
            return root.val == arr[i] and root.left is None and root.right is None
        if root.val != arr[i]:
            return False
        return self.dfs(root.left, arr, i + 1) or self.dfs(root.right, arr, i + 1)


if __name__ == '__main__
