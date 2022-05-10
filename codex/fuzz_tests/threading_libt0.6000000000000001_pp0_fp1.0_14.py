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

INT_MIN = -2147483648
INT_MAX = 2147483647

def createTree(arr):
    n = len(arr)
    root = None
    for i in range(n):
        if arr[i] == -1:
            continue
        if i == 0:
            root = TreeNode(arr[i])
            continue
        ptr = root
        j = 0
        while j < i:
            if i % 2 == 0:
                if ptr.left is None:
                    ptr.left = TreeNode(arr[i])
                    break
                ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right
