import signal
# Test signal.setitimer() in an environment where wait() and waitpid() calls sometimes block.
import sys
import os
import time
import commands
import threading
import unittest
import warnings
import errno

if hasattr(signal, 'setitimer'):
    warn_once = True
    # A simple background thread which wakes itself up every n seconds.
    class LoopThread(threading.Thread):
        def __init__(self, n):
   
