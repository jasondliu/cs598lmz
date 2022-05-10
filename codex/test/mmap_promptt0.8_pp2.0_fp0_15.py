import mmap
# Test mmap.mmap.flush()
# http://bugs.python.org/issue3866
import os
import signal
import tempfile
import threading
import time

SIGNAL = signal.SIGUSR1

num_threads = None

