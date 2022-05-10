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

    i = 1
    while(i<len(list)):
        if list[i] == -1:
            i += 1
            continue
        else:
            break

    ltree = createTree(list[i:])
    root.left = ltree

    rlist = list[i+1:]
    rtree = createTree(rlist)
    root.right = rtree

    return root

def printTree(root):
    if root==None:
        return
    print(root.val, end=" ")

