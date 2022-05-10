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

    if len(arr)==0:
        return None

    root = TreeNode(arr[0])
    i = 0
    q = [root]
    while(len(q)):
        temp = q.pop(0)
        i += 1
        if i<len(arr):
            if arr[i] is not None:
                temp.left = TreeNode(arr[i])
                q.append(temp.left)
            else:
                temp.left = None
        i += 1
        if i<len(arr):
            if arr[i] is not None:
                temp.right = TreeNode(arr[i])
               
