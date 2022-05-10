import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
print('Main thread')

# The output of this program is unpredictable.
# On some platforms, the output may be:
# Main thread
# Thread 1
# Thread 2
# On other platforms, the output may be:
# Thread 1
# Thread 2
# Main thread
# Or any other combination.

# In this example, we are using the threading module to create and start two threads,
# which will run concurrently with the main thread.
# Each thread executes a lambda function that writes a line to standard output.
# The main thread also writes a line to standard output.
# Because the threads are running concurrently with the main thread,
# the output of the program is unpredictable.

# The global interpreter lock, or GIL, is a mechanism that prevents multiple native threads
# from executing Python bytecodes at once.
# This lock is necessary because CPython’s memory management is not thread-safe.
# (However, since the GIL exists,
