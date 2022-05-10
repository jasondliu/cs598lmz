import gc, weakref
import contextlib

from collections import namedtuple

class Tree(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children

def make_tree(depth):
    if depth > 0:
        return Tree(depth, [make_tree(depth-1), make_tree(depth-1)])
    else:
        return Tree(depth, [])

def tree_sum(t):
    return t.value + sum(tree_sum(c) for c in t.children)

def main():
    tree = make_tree(5)
    print("Tree sum:", tree_sum(tree))


if __name__ == '__main__':
    main()
