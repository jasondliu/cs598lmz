import sys, threading
threading.Thread(target=lambda: sys.stderr.write("Hello\n")).start()


# ------------
# Threads with a Global Interpreter Lock (GIL)
# ------------
# Python is not thread safe.
# Each Python thread has a lock around its execution, allowing only one thread to be active at a time.
# If a thread wants to wait for another thread to finish, it will release its lock and another thread
# can take over.
# The GIL is a single lock around the Python interpreter.
# When a thread releases its lock, the GIL can be acquired by another thread.
# The GIL prevents multiple threads from executing bytecode at once.
# This is good for I/O-bound tasks where CPU time is less important.
# ------------
# Python Threading Options
# ------------
# Python Standard Library (threading)
# multiprocessing (spawns new processes)
# gevent (cooperative concurrency based on coroutines)
# Twisted (event-driven networking framework)
# ------------
# Threading - Example 1
# ------------
# Python provides a built-in module called threading that contains classes
