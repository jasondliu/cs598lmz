import select
# Test select.select()

import socket
import time
import threading

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

def dowork():
    start = time.time()
    for _ in range(5):
        slow_systemcall()

    print('Time taken in seconds -', time.time() - start)

NUM_THREADS = 2

threads = []
for i in range(NUM_THREADS):
    thread = threading.Thread(target=dowork)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Time taken in seconds - 1.0049355030059814
# Time taken in seconds - 1.0039658451080322

# Total time taken is more than twice as slow as using only one thread.
# The reason is that the GIL prevents threads from running in parallel.

# This is the case for most Python programs running in CPython, where the GIL will limit you to
# a maximum of one thread per CPU core
