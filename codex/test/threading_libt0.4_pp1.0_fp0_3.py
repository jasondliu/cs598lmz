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

def buildTree(arr):
    root = Node(arr[0])
    arr.pop(0)
    stack = [root]
    while len(arr) > 0:
        temp = stack[0]
        stack.pop(0)
        if arr[0] == -1:
            temp.left = None
            arr.pop(0)
        else:
            temp.left = Node(arr[0])
            arr.pop(0)
            stack.append(temp.left)
        if len(arr) == 0:
            break
        if arr[0] == -1:
            temp.right = None
            arr.pop(0)
