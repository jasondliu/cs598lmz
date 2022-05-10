import _struct
import re
import sys
import tempfile
import shutil

from os import remove, rmdir
from os.path import join, exists, split

from urllib import urlopen, unquote, urlretrieve, quote
from urlparse import urlparse

from time import time

# Parse manifest
def manifest_check(manifest):
    entries = manifest.split('\n')
    manifest_dict = {}
    for entry in entries:
        entry = entry.split(' ')
        if len(entry) == 2:
            manifest_dict[entry[0]] = entry[1]
    return manifest_dict

# Check attributes
def is_dir(path):
    '''returns True if path is a directory'''
    return path.endswith('/')

def is_file(path):
    '''returns True if path is a file'''
    return not path.endswith('/')

def is_link(path):
    '''returns True if path is a symbolic link'''
    return path.startswith('@')
