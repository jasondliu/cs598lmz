import threading
threading.stack_size(67108864) # 64MB stack
# xrange = range

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def read_tree():
    global n, tree
    n = int(input())
    tree = [Node(i) for i in range(n)]
    for _ in range(n-1):
        parent, child = map(int, input().split())
        tree[parent].add_child(tree[child])

def postorder(node):
    for c in node.children:
        postorder(c)
    postorder_list.append(node.data)

def lca(u, v):
    while u != v:
        if u > v:
            u >>= 1
        else:
            v >>= 1
    return u

