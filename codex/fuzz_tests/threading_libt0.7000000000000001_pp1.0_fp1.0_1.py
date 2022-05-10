import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def serialize(root):
    output = []
    def helper(node):
        if not node:
            return
        output.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return output


def deserialize(data):
    if not data: return
    root = TreeNode(data[0])
    def helper(node, pos):
        if pos == len(data):
            return
        if data[pos] < node.val:
            node.left = TreeNode(data[pos])
        else:
            node.right = TreeNode(data[pos])
        helper(node.left, pos
