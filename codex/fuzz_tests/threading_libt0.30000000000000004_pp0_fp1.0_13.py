import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preorder, inorder, preStart, preEnd, inStart, inEnd):
    if preStart > preEnd or inStart > inEnd:
        return None
    root = Node(preorder[preStart])
    rootIndex = -1
    for i in range(inStart, inEnd + 1):
        if inorder[i] == root.data:
            rootIndex = i
            break
    root.left = buildTree(preorder, inorder, preStart + 1, preStart + rootIndex - inStart, inStart, rootIndex - 1)
    root.right = buildTree(preorder, inorder, preStart + rootIndex - inStart + 1, preEnd
