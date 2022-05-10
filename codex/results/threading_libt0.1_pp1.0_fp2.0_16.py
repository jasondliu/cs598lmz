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
    frontier = [root]
    while i<len(list):
        next = []
        for u in frontier:
            if list[i]!=None:
                left = TreeNode(list[i])
                u.left = left
                next.append(left)
            i+=1
            if i>=len(list):
                break
            if list[i]!=None:
                right = TreeNode(list[i])
                u.right = right
                next.append(right)
            i
