import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from __future__ import print_function

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val,end=' '),
 
        # now recur on right child
        printInorder(root.right)

def isBST(root, min_val=-1, max_val=10000000000):
	if root is None:
		return True

	if root.val < min_val or root.val > max_val:
		return False

	return
