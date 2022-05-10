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

def treeInput():
    n = int(input())
    if n == 0:
        return None
    root = TreeNode(int(input()))
    q = [root]
    while len(q) != 0:
        curr = q.pop(0)
        val = input()
        if val != 'N':
            left = TreeNode(int(val))
            curr.left = left
            q.append(left)
        val = input()
        if val != 'N':
            right = TreeNode(int(val))
            curr.right = right
            q.append(right)
    return root

def treePrint(root):
    if root
