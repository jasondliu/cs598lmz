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

def insert(root, key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current
