import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
        cur = q[front]
        front += 1
        left = lst[0]
        lst = lst[1:]
        if left != -1:
            cur.left = TreeNode(left)
            q.append(cur.left)
        right = lst[0]
        lst = lst[1:]
