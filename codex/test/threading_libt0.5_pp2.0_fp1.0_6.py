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

def createTree(list):
    if list[0] == -1:
        return None
    root = TreeNode(list[0])
    i = 1
    q = [root]
    while q:
        curr = q.pop(0)
        if list[i] != -1:
            curr.left = TreeNode(list[i])
            q.append(curr.left)
        i += 1
        if list[i] != -1:
            curr.right = TreeNode(list[i])
            q.append(curr.right)
        i += 1
    return root

