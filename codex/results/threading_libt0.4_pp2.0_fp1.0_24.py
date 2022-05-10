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

def buildTree(inOrder, preOrder, inStrt, inEnd):
    if inStrt > inEnd:
        return None
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    if inStrt == inEnd:
        return tNode
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)
    return tNode

def search(arr, start, end, value):
   
