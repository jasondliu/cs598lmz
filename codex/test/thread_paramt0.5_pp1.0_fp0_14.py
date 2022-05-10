import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()

# Python's threading library is built on top of native OS threads, so it can't be
# used to parallelize CPU-bound tasks, since the OS thread can only run on one CPU
# at a time.

# If you want to parallelize CPU-bound tasks, you'll need to use the multiprocessing
# module, which uses multiple processes instead of threads.

# The multiprocessing module provides a Pool class that can be used to run multiple
# worker processes.

# Each worker process runs in parallel and is passed arguments through a Queue.

# A Pool object can be used as a context manager.

import multiprocessing

# This function will be run in a worker process.
def worker(n):
    return n * n

# Create a pool of four worker processes.
with multiprocessing.Pool(4) as pool:
    # Print the result of 10 tasks.
    for _ in range(10):
        print(pool.apply(worker, (2,)))

# The apply method blocks until the
