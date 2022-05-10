import threading
threading.stack_size(1024*1024)

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

