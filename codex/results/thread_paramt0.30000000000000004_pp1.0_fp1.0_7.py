import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from threading.Thread\n")).start()

# The threading module is a wrapper around the low-level thread module.
# The thread module is a low-level API for working with threads.
import thread
thread.start_new_thread(lambda: sys.stdout.write("Hello from thread.start_new_thread\n"), ())

# The multiprocessing module is a wrapper around the low-level multiprocessing module.
# The multiprocessing module is a low-level API for working with processes.
import multiprocessing
multiprocessing.Process(target=lambda: sys.stdout.write("Hello from multiprocessing.Process\n")).start()

# The threading and multiprocessing modules are high-level APIs for working with threads and processes.
# The thread and multiprocessing modules are low-level APIs for working with threads and processes.
# The threading module is a wrapper around the low-level thread module.
# The multiprocessing module is a wrapper around the low-level multiprocessing module.

