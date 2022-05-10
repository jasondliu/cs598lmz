import ctypes
import ctypes.util
import threading
import sqlite3
import argparse
import sys
import time
import os
import traceback
import uuid
import json
import re
import hashlib

# from pprint import pprint

def get_all_files(path):
    """
    Walks the directory and returns all the files in it.
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

def get_all_files_and_contents(path):
    """
    Walks the directory and returns all the files in it, together with their
    contents.
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            with open(os.path.join(dirpath, filename), 'rb') as f:
                files.append((os.path.join(dirpath, filename), f.read()))
    return files

