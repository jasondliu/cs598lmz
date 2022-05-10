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
    front = 0
    while(front<=i and i<n):
        temp = q[front]
        front += 1

        item = list[i]
        if item!=None:
            temp.left = TreeNode(item)
            q.append(temp.left)

        i += 1
        
        if i>=n:
            break
        
        item = list[i]
