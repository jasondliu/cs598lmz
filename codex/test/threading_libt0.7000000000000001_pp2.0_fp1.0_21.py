import threading
threading.stack_size(1 << 25)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def read():
    global root
    return map(int, sys.stdin.readline().strip().split())

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    sys.stdout.write(str(root.key) + " ")
    inOrder(root.right)

def isBST(root):
    if root is None:
        return True
    if root.left is not None and root.left.key > root.key:
        return False
    if root.right is not None and root.right.key < root.key:
        return False
    if not isBST(root.left) or not isBST(root.right):
        return False
    return True

def createBST(a):
    global root
    root = Node(a[0])
