import threading
threading.stack_size(67108864)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    if root is None:
        return True
    if root.left is not None and root.left.data > root.data:
        return False
    if root.right is not None and root.right.data < root.data:
        return False
    if not isBST(root.left) or not isBST(root.right):
        return False
    return True

def isBSTUtil(root, prev):
    if root is None:
        return True
    if not isBSTUtil(root.left, prev):
        return False
    if prev[0] is not None and root.data <= prev[0]:
        return False
    prev[0] = root.data
    return isBSTUtil(root.right, prev)

def isBST2(root):
    prev = [None]

