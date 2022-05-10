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
    while i < len(list):
        parent = q.pop(0)
        child = TreeNode(list[i])
        parent.left = child
        q.append(child)
        i += 1
        if i >= len(list):
            break
        child = TreeNode(list[i])
        parent.right = child
        q.append(child)
        i += 1
    return root

def printTree(root):
    if root == None:
        return
   
