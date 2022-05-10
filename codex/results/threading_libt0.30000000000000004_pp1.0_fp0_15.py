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
    while i < len(list):
        curr = queue.pop(0)
        if list[i] is not None:
            curr.left = TreeNode(list[i])
            queue.append(curr.left)
        i += 1
        if i >= len(list):
            break
        if list[i] is not None:
            curr.right = TreeNode(list[i])
            queue.append(curr.right)
        i += 1
    return root
