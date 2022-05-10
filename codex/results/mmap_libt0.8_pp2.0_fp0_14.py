import mmap
import os
class list:
    def __init__(self):
        self.strings = ''
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter == self.strings:
            raise StopIteration
        self.counter += 1
        return self.lines[self.counter - 1]
    def append(self, str):
        self.strings += 1
        self.lines.append(str)
    def sort(self):
        self.lines.sort()
def unsorted_items(dir):
    with open(dir + '/' + 'mmap.data', 'r') as file:
        mmap_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        temp_file = open(dir + '/' + 'temp_mmap.data', 'w')
        block_size = 1024
        block_numbers = math.ceil(os.path.getsize(dir + '/' + 'mmap.data') / block_
