import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os
import re
import sys
import time


class Queue(object):
    def __init__(self):
        self.data = []
        self.lock = threading.RLock()
        self.new = None
        self.waiting = threading.Condition()

    def __len__(self):
        self.lock.acquire()
        try:
            return len(self.data)
        finally:
            self.lock.release()

    def enqueue(self, item):
        self.lock.acquire()
        try:
            self.data.append(item)
            self.waiting.notify()
        finally:
            self.lock.release()

    def dequeue(self):
        self.lock.acquire()
        try:
            while True:
                if self.data:
                    return self.data.pop()
                else:
                    self.waiting.wait()
        finally:
            self.lock.release()

    def wait(self):
        self.lock.acquire()
        try
