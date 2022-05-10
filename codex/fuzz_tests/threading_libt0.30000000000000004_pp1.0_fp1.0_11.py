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

def createTree(arr):

    if len(arr) == 0:
        return None

    root = TreeNode(arr[0])
    i = 0
    l = len(arr)

    q = [root]
    while i < l:

        temp = q.pop(0)

        if 2 * i + 1 < l and arr[2 * i + 1] is not None:
            temp.left = TreeNode(arr[2 * i + 1])
            q.append(temp.left)

        if 2 * i + 2 < l and arr[2 * i + 2] is not None:
            temp.right = TreeNode(arr[2 * i + 2])
            q
