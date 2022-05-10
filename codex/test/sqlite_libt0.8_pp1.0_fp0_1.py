import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import random

class DataNode:
    data = None
    next = None

class List:
    _head = None
    _tail = None

    def add(self, data):
        if self.empty():
            self._head = DataNode()
            self._head.data = data
            self._tail = self._head
        else:
            temp = DataNode()
            temp.data = data
            temp.next = self._head
            self._head = temp

    def empty(self):
        return self._head is None

    def __iter__(self):
        self._cur = self._head
        return self

    def __next__(self):
        if self._cur is None:
            raise StopIteration
        else:
            n = self._cur
            self._cur = self._cur.next
            return n.data

class KMP:
    def __init__(self):
        self._db = sqlite3.connect(":memory:", check_same_thread=False)
        self._db
