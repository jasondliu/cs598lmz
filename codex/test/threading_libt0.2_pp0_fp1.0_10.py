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
    if len(list)==0:
        return None
    root = TreeNode(list[0])
    i = 1
    frontier = deque()
    frontier.append(root)
    while frontier:
        upper_node = frontier.popleft()
        if i<len(list) and list[i] is not None:
            upper_node.left = TreeNode(list[i])
            frontier.append(upper_node.left)
        i += 1
        if i<len(list) and list[i] is not None:
            upper_node.right = TreeNode(list[i])
