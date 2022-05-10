import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()

# --------------------------
# The output is:
# Hello from thread 1
# Hello from thread 2
# --------------------------

# The threads are executed in parallel and the output is mixed.
# This is a simple example of multithreading, but it is not useful in practice.
# The following example shows how to use a thread to compute the sum of the integers from 1 to 1000000.

import threading

def worker():
    """thread worker function"""
    total = 0
    for i in range(1000000):
        total += i
    print(total)

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# --------------------------
# The output is:
# 1784293664
# 1784293664
# 1784293664
# 17842936
