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
    frontier = deque()
    frontier.append(root)
    while i < len(list):
        if list[i] == "null":
            frontier.popleft()
            i += 1
        else:
            top = frontier[0]
            if top.left is None:
                top.left = TreeNode(list[i])
                i += 1
                frontier.append(top.left)
            else:
                top.right = TreeNode(list[i])
                i += 1
