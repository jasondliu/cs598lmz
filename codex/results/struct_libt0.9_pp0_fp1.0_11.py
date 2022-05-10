import _struct
import _pickle
import errno
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import time
import types

sys.path.insert(1, os.path.join(os.path.dirname(__file__), ...).replace('\\', '/'))

NODE_DISCONNECTED = 0
NODE_RUNNING = 1
NODE_STARTING = 2

g_contexts = {}
g_queue = []
g_thread = None
g_terminate = False

def dump(val):
    t = type(val)
    if t == type(None):
        return None
    elif t == bool:
        return val
    elif t == int:
        return val
    elif t == float:
        return val
    elif t == str:
        return val
    elif t == bytes:
        return val
    elif t == list:
        return [dump(x) for x in val]
    elif t == set:
        return {dump(x
