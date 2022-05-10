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

def insert(root, data):
    if root == None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data, end = ' ')
    inOrder(root.right)

def preOrder(root):
    if root == None:
        return
    print(root.data, end = ' ')
    preOrder(root.left)
