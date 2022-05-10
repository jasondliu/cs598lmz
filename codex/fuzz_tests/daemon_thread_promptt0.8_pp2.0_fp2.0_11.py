import threading
# Test threading daemon

THREADS = 2

def f(x, d=2):
    for i in xrange(10*d):
        x = ((x<<1)&((1<<x.bit_length())-1))|((x>>(x.bit_length()-1))&1)
    print x

for d in xrange(THREADS):
    t = threading.Thread(target = f, args = (2,d+1))
    t.daemon = True
    t.start()

# Wait for all threads to terminate.
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
print 'main thread done'

# File pythdaemon.py
import atexit
import signal
import sys
import threading

class Daemon(object):
    """
    A generic daemon class.
    
    Usage: subclass the Daemon class and override the run() method
    """
    def __init__(self, pidfile, stdin='/dev/
