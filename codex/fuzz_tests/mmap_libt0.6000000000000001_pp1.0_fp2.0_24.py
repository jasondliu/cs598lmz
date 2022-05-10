import mmap
import os
import re
import sys
import time

def get_mmap_size(filepath):
    """
    The size of mmap'd file must be a multiple of the page size, which is
    usually 4KB. This function returns the size of the file rounded up to the
    nearest page size.
    """
    page_size = os.sysconf('SC_PAGE_SIZE')
    fsize = os.path.getsize(filepath)
    return page_size * ((fsize + page_size - 1) // page_size)

def file_exists(filepath):
    if not os.path.exists(filepath):
        print('File "{}" does not exist.'.format(filepath))
        return False
    return True

def main():
    if len(sys.argv) != 2:
        print('Usage: {} <filepath>'.format(sys.argv[0]))
        return
    filepath = sys.argv[1]
    if not file_exists(filepath):
        return
    size = get
