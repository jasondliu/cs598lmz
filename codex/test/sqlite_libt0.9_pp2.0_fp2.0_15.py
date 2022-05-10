import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time

# If you want NLTK to use local core libraries, you will need to change this value
default_core_lib = '/usr/local/lib/libnltk_lite.so'

# Point NLTK libraries to the local directory and then import
ctypes.cdll.LoadLibrary(default_core_lib)
nltk = imp.load_module('nltk', *imp.find_module('nltk'))
taggers = imp.load_module('taggers', *imp.find_module('taggers', [nltk_path]))
tokenizer = imp.load_module('tokenizer', *imp.find_module('tokenizer', [nltk_path]))
probability = imp.load_module('probability', *imp.find_module('probability', [nltk_path]))
metrics = imp.load_module('metrics', *imp.find_module('metrics', [nltk_path]))


