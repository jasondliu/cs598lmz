import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Trie(object):
    def __init__(self):
        self.root = {}

    def add(self, word):
        d = self.root
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['$'] = True

    def find(self, word):
        d = self.root
        for c in word:
            if c in d:
                d = d[c]
            else:
                return False
        return '$' in d

    def nodes(self):
        return self.root

class TrieThread(threading.Thread):
    def __init__(self, trie, path):
        threading.Thread.__init__(self)
        self.trie = trie
        self.path = path

    def run(self):
        for line in open(self.path):
            self.trie.add(line.strip())

