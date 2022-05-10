import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTree(list):
    if len(list) == 0:
        return None
    root = TreeNode(list[0])
    i = 1
    frontier = deque()
    frontier.append(root)
    while frontier:
        levelSize = len(frontier)
        for _ in range(levelSize):
            node = frontier.popleft()
            if i >= len(list):
                return root
            if list[i] is not None:
                node.left = TreeNode(list[i])
                frontier.append(node.left)
            i += 1
            if i >= len(list):
                return root
            if list[i] is not None
