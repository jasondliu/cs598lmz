import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def countNodes(root):
    if root is None:
        return 0
