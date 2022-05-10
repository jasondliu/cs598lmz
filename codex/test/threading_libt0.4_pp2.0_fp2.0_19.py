import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(list):
    if list[0] == -1:
        return None
    head = TreeNode(list[0])
    lst = list[1:]
    q = [head]
    front = 0
    while front < len(q):
        curr = q[front]
        front += 1
        if lst and lst[0] != -1:
            curr.left = TreeNode(lst[0])
            q.append(curr.left)
            lst.pop(0)
