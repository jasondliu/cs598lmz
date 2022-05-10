import mmap
import re
import time
import sys

def get_content_map(fname):
    f = open(fname, "rb")
    try:
        return mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    finally:
        f.close()

def get_content_file(fname):
    f = open(fname, "rb")
    try:
        return f.read()
    finally:
        f.close()

def get_content_file_by_line(fname):
    f = open(fname, "rb")
    try:
        return f.readlines()
    finally:
        f.close()

def get_usage():
    return '''------------------------------------
| Use: python test_re.py <file> |
------------------------------------
'''

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fname = sys.argv[1]
