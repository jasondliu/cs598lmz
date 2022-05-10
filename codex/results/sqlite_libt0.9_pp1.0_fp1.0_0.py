import ctypes
import ctypes.util
import threading
import sqlite3

#connection_lock = threading.Lock()

class KeywordTree(object):
    """A class for a keyword tree. When adding keywords, the keyword tree splits
    up the keyword in a tree form so we can search efficiently."""
    def __init__(self):
        """Initializes a new KeywordTree object"""
        self.root = dict()
        self.hash = dict()

    def add_keyword(self, keyword, value=None):
        """Adds a keyword to the tree. now it only supports a value, but we could
        bind values to keywords so that the terminal crumbs can have a list of
        values."""
        if keyword in self.hash:
            return
        self.hash[keyword] = value
        current = self.root
        for c in keyword:
            current = current.setdefault(c, {})

    def has_keyword(self, keyword):
        """Checks if a keyword is added to the tree."""
        return keyword in self.hash

    def split_keyword(self, keyword):
        """Splits a keyword into
