import ctypes
import ctypes.util
import threading
import sqlite3
import platform
import time
import string
import random
import os.path
import subprocess
import sys
import signal
import re
# import pyperclip

def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

