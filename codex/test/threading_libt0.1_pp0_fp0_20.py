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
            i += 1
            continue
        parent = frontier.popleft()
        leftChild = TreeNode(list[i])
        parent.left = leftChild
        frontier.append(leftChild)
        i += 1
        if i == len(list):
            break
        if list[i] == "null":
            i += 1
