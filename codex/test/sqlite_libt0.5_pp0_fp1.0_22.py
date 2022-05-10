import ctypes
import ctypes.util
import threading
import sqlite3


class Node:
    def __init__(self, index, parent, value):
        self.index = index
        self.parent = parent
        self.value = value
        self.children = []

class Trie:
    def __init__(self):
        self.root = Node(0, None, 0)
        self.node_count = 1
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE nodes (index INTEGER PRIMARY KEY, parent INTEGER, value INTEGER)")
        self.db.execute("CREATE TABLE prefixes (index INTEGER PRIMARY KEY, prefix TEXT)")
        self.db.execute("CREATE TABLE words (index INTEGER PRIMARY KEY, word TEXT)")

    def insert(self, word):
        current_node = self.root
        for c in word:
            for child in current_node.children:
                if child.value == ord(c):
                    current_node = child
                    break
