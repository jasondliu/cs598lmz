import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 3\n')).start()

# -------------------------------------------------------------
# Parallel Processing
# -------------------------------------------------------------

# The multiprocessing module allows you to spawn processes in much that same
# manner than you can spawn threads with the threading module.

# The difference is that threads run in the same memory space, while processes
# have separate memory. This makes it a bit more difficult to share objects
# between processes with multiprocessing.

# Because of this, the multiprocessing module allows you to initialize a
# separate server process to act as a manager for shared objects.

# The following example demonstrates the use of a manager to create a shared
# dictionary that can be updated by separate processes:

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1
