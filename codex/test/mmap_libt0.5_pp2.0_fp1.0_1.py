import mmap
from collections import deque

class mmap_queue(object):
    def __init__(self, filename=None, size=10):
        self.filename = filename
        self.size = size
        self.queue = deque()
        self.mm = None

    def open(self):
        self.mm = mmap.mmap(-1, self.size)
        return self.mm

    def close(self):
        self.mm.close()

    def write(self, value):
        self.queue.append(value)
        if len(self.queue) > self.size:
            self.queue.popleft()
        self.mm.seek(0)
        self.mm.write(''.join(self.queue))

    def read(self):
        self.mm.seek(0)
        return self.mm.read(self.size)

    def read_all(self):
        self.mm.seek(0)
        return self.mm.read()

if __name__ == '__main__':
    import time
    import random
