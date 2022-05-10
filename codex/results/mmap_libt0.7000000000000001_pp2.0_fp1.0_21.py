import mmap
import traceback

class CircularBuffer(object):
    def __init__(self, size_max):
        self.max = size_max
        self.data = {}
        self.cur = 0
        self.size = 0

    def append(self, x):
        if self.size < self.max:
            self.data[self.cur] = x
            self.size += 1
        else:
            self.data[self.cur] = x
        self.cur = (self.cur + 1) % self.max

    def get(self):
        return [self.data[(self.cur - i) % self.max] for i in range(min(self.size, self.max))]

class Logger:
    def __init__(self):
        self.log_list = []
        self.log_file = None
        self.log_mmap = None
        self.log_mmap_size = 0
        self.log_mmap_index = 0
        self.log_mmap_offset = 0
        self.log
