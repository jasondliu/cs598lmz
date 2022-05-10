import weakref
import sys


class Trie:
    def __init__(self):
        self.trie = {}
        self.word_end = '_end_'

    def insert(self, word):
        if not word:
            return
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr[self.word_end] = self.word_end

    def contains(self, word):
        curr = self.trie
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]

        return self.word_end in curr

    def starts_with(self, prefix):
        curr = self.trie
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True


class Node:
    def __init__(self, val):
        self.val = val

