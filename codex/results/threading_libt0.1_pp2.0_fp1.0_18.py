import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
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
    l = createTree(list[1])
    r = createTree(list[2])
    head.left = l
    head.right = r
    return head

def printTree(head):
    if head == None:
        return
    print(head.val, end = ' ')
    printTree(head.left)
    printTree(head.right)

def inorder(head):
    if head == None:
        return
    inorder(head.left)
    print
