import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(arr):
    n = len(arr)
    if n == 0:
        return None
    root = Node(arr[0])
    j = 0
    list = []
    list.append(root)
    i = 1
    while j < len(list) and i < n:
        parent = list[j]
        child = Node(arr[i])
        if parent.left == None:
            parent.left = child
            list.append(child)
        else:
            parent.right = child
            list.append(child)
            j += 1
        i += 1
    return root

def inorder(root):
    if root == None:
