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
    s = input().strip().split()
    if len(s) == 0:
        return None
    i = 0
    root = Node(int(s[i]))
    q = [root]
    i += 1
    while len(q) > 0 and i < len(s):
        curr = q[0]
        q.pop(0)
        curr.left = Node(int(s[i]))
        q.append(curr.left)
        i += 1
        if i >= len(s):
            break
