from bz2 import BZ2Decompressor
BZ2Decompressor().__init__

import gzip
gzip.open

import bz2
bz2.open

import zipfile
zipfile.zipfile

import zlib
zlib.decompressobj

class Queue(object):
    def __init__(self, *args):
        self._queue = list(*args)
    def pop(self, *args):
        return self._queue.pop(*args)
    def __len__(self):
        return len(self._queue)

import Queue
Queue.Queue

class Queue(object):
    def __init__(self, *args):
        self._queue = list(*args)
    def put(self, *args):
        self._queue.append(*args)
    def __len__(self):
        return len(self._queue)

import Queue
Queue.LifoQueue

class Queue(object):
    def __init__(self, *args):
        self._queue = []
    def put(self, *args):
        self._queue.append(*args)

