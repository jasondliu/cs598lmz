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
    if len(list) == 0:
        return None
    root = TreeNode(list[0])
    i = 1
    queue = [root]
    while(len(queue)>0 and i<len(list)):
        currNode = queue[0]
        queue.pop(0)
        currNode.left = TreeNode(list[i]) if list[i] != -1 else None
        if currNode.left:
            queue.append(currNode.left)
        i += 1
        if i >= len(list):
            break
