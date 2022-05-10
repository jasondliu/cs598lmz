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
    if list[0] == -1:
        return None
    root = TreeNode(list[0])
    i = 1
    q = [root]
    while q and i < len(list):
        current = q.pop(0)
        if list[i] != -1:
            leftChild = TreeNode(list[i])
            current.left = leftChild
            q.append(leftChild)
        i += 1
        if list[i] != -1:
            rightChild = TreeNode(list[i])
            current.right = rightChild
            q.append(rightChild)
        i += 1
    return root


