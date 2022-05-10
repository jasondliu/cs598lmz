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

def createTree(list):

    if len(list)==0:
        return None

    root = TreeNode(list[0])
    i = 0
    n = len(list)

    q = [root]
    f = 0
    while f<=n:
        temp = q[0]
        q.pop(0)
        f += 1

        if 2*i+1<n and list[2*i+1] is not None:
            temp.left = TreeNode(list[2*i+1])
            q.append(temp.left)

        if 2*i+2<n and list[2*i+2] is not None:
            temp
