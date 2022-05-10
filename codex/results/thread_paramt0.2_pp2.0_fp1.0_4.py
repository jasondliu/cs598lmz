import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# The output of this program may vary depending on the operating system and
# version of Python.  On my machine, the output is:
#
# Hello from thread 1
# Hello from thread 2
#
# If you run this program multiple times, you may see a different ordering of
# the output.  (On Windows, it's possible that the threads will run
# simultaneously, interleaving their output.)

# -----------------------------------------------------------------------------
# Threads communicate using shared memory
# -----------------------------------------------------------------------------

# The two threads we just created are completely independent: they run in
# parallel, they don't share any memory, and they can't communicate.  To share
# data between threads, you can use a global variable (a named variable that is
# defined outside of any function or class), though this is generally
# discouraged in Python.

# Here's an example of using a global variable to communicate between threads.
# We'll define a global variable, x,
