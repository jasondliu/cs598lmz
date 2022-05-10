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

def signal_handler(num):
    print "Signal handler in thread %s" % threading.current_thread().ident
    global num_threads
    num_threads -= 1

signal.signal(SIGNAL, signal_handler)

def test(file, offset, size):
    global num_threads

    pid = os.getpid()
    print "Thread %s: starting" % threading.current_thread().ident

    m = mmap.mmap(file.fileno(), size, access=mmap.ACCESS_WRITE,
                  offset=offset)
    try:
        time.sleep(0.1)
        os.kill(pid, SIGNAL)
        m.flush()
        m.seek(0)
        s = m.read(size)
        assert len(s) == size
    finally:
