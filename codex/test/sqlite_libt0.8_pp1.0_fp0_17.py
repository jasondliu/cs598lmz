import ctypes
import ctypes.util
import threading
import sqlite3
import argparse
import logging
import os
import sys
import re
import subprocess
import collections
import inspect
import shutil
import tempfile

logger = logging.getLogger(__name__)

def dbpath(path):
    if path == ':memory:': return path
    if path.startswith('~'): path = os.path.expanduser(path)
    return os.path.abspath(path)


