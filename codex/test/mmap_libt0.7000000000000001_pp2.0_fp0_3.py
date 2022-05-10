import mmap
import os
import sys
import time

def generate_unique_dir_name(prefix):
    return os.path.join(prefix, str(time.time()))

def generate_unique_fname(prefix):
    return prefix + '.' + str(time.time())

def get_size(fname):
    return os.path.getsize(fname)

def get_mtime(fname):
    return os.path.getmtime(fname)

def get_modified_size(fname):
    return get_mtime(fname), get_size(fname)

def get_modified_size_list(fname_list):
    return [get_modified_size(fname) for fname in fname_list]

def get_modified_size_list_fname(fname):
    if not os.path.exists(fname):
        return []
    with open(fname) as f:
        return [[float(x) for x in line.split()] for line in f]

