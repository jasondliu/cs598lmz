import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Vertex:
    def __init__(self, value, parent, depth):
        self.value = value
        self.parent = parent
        self.depth = depth
        self.children = []
        self.is_visited = False


class Tree:
    def __init__(self, root):
        self.root = root

    def add_child(self, parent_node, child_node):
        parent_node.children.append(child_node)


def build_tree(n, edges):
    nodes = [Vertex(i, None, 0) for i in range(n)]

    tree = Tree(nodes[0])
    for edge in edges:
        tree.add_child(nodes[edge[0]], nodes[edge[1]])
