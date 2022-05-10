import ctypes
import ctypes.util
import threading
import sqlite3 as xsql
from subprocess import Popen, PIPE, STDOUT

class synonym:
    def __init__(self, word, syn=""):
        self.word = word
        self.syn = syn
        self.cls = "NULL"
        self.z_score = -1


class iC(iW):
    def __init__(self, word, wordclass = "NULL"):
        super().__init__(word)
        self.wordClass = wordclass


class tup(object):
    def __init__(self, tweet, ind):
        self.tweet = tweet
        self.index = ind

class ThreadedClient(threading.Thread):

    def __init__(self, queue, method, start=0, end=None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.method = method
        self.start = start
        self.end = end

    def run(self):
        for i in range(self.start, self.end):
            #print("Thread
