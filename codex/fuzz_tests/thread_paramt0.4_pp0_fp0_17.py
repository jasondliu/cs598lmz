import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# The output of this program will be interleaved, because the two threads run
# simultaneously.

# The following program uses the threading module to implement a simple
# “thread pool”, where a fixed number of threads are created and work items are
# added to a queue. The threads wait for work items and process them until the
# main thread exits.

import threading
import time

def worker():
    """thread worker function"""
    print 'Worker'
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# The worker function is defined as a Python callable that prints a message and
# waits for one second. Five threads are created and started.

# When the main thread exits, the program is terminated.

#
