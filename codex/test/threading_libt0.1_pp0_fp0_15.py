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
        if list[i] is not None:
            temp = TreeNode(list[i])
            frontier.append(temp)
        frontier.popleft()
        if list[i] is not None:
            if frontier[0].left is None:
                frontier[0].left = temp
            else:
                frontier[0].right = temp
        i += 1
    return root

