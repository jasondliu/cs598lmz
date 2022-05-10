import threading
threading.stack_size(512*1024)
sys.setrecursionlimit(10**6)

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        root = node(data)
    elif data > root.data:
        if root.right is None:
            root.right = node(data)
        else:
            insert(root.right, data)
    elif data < root.data:
        if root.left is None:
            root.left = node(data)
        else:
            insert(root.left, data)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):

