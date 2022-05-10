import mmap
import sys
import time
import random

# def read_file(file_name):
#     with open(file_name, 'r+') as f:
#         mm = mmap.mmap(f.fileno(), 0)
#         print(mm.readline())
#         mm.seek(0)
#         print(mm.readline())
#         mm.close()
#         f.close()

def read_file(file_name):
    with open(file_name, 'r+') as f:
        mm = mmap.mmap(f.fileno(), 0)
        while True:
            line = mm.readline()
            if not line:
                break
            print(line)
        mm.close()
        f.close()

def write_file(file_name):
    with open(file_name, 'w+') as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.write(b'Hello Python!')
        mm.close()
        f.close()

