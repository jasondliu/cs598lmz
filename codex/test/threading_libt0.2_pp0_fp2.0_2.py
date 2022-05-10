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
        # print([current_node.val if current_node else None for current_node in frontier])
        current_node = frontier.popleft()
        if i<len(list) and list[i] is not None:
            left_child = TreeNode(list[i])
            current_node.left = left_child
            frontier.append(left_child)
        i += 1
