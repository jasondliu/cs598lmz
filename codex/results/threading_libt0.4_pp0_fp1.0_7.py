import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None
    
    def search(self, x):
        return self._search(self.root, x)
    
    def _search(self, p, x):
        if p == None:
            return None
        if x < p.info:
            return self._search(p.lchild, x)
        elif x > p.info:
            return self._search(p.rchild, x)
        else:
            return p
    
    def insert(self, x):
        self.root = self
