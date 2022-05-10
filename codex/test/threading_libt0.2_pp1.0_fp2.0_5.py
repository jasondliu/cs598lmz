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

def buildTree(t):
    if t == None:
        return None
    currData = t[0]
    root = Node(currData)
    size = len(t)
    i = 1
    while i < size:
        currData = t[i]
        if currData == -1:
            break
        if currData < root.data:
            root.left = Node(currData)
            q.append(root.left)
        else:
            root.right = Node(currData)
            q.append(root.right)
        i += 1
    buildTree(t[i:])
    return root

