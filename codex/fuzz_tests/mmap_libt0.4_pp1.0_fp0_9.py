import mmap
import os
import re
import subprocess
import sys
import time

from . import utils

# TODO: move to utils
def _get_file_size(file_path):
    file_size = os.path.getsize(file_path)
    return file_size

def _get_file_content(file_path):
    file_size = _get_file_size(file_path)
    with open(file_path, 'r') as f:
        m = mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_READ)
        return m

def _get_file_content_in_lines(file_path):
    file_size = _get_file_size(file_path)
    with open(file_path, 'r') as f:
        m = mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_READ)
        return m.readlines()

def _get_file_content_as_string(file_path):
   
