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

print "--------------------------------------------"
print "TPM2.0 DBG"
print "--------------------------------------------"
# print "TODO"

# print "TODO: Check if the program is running as sudo or root"
# print "TODO: Check if the script is running from the right directory"
# print "TODO: Check if the TPM is turned on"
# print "TODO: Check if the tool is installed"
# print "TODO: Check if the files are present"

# TODO: Check if the program is running as sudo or root
# TODO: Check if the script is running from the right directory
# TODO: Check if the TPM is
