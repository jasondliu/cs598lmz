import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Executing this program yields a result like this, with the two lines interleaved:
# $ python3 stdio_threads.py
# Hello from thread 1
# Hello from thread 2

# In the program above, we used the threading module to create two threads that write to standard output. Since the two threads run concurrently, the lines produced by each thread may appear in any order in the final result.
# To demonstrate this, the program is run again. This time, thread 2’s message appears first:
# $ python3 stdio_threads.py
# Hello from thread 2
# Hello from thread 1

# The issue with standard output is that it is not thread-safe. Threads can interleave their output, resulting in messages from different threads being interleaved.

# The threading module provides a simple way to make functions run in separate threads.
# The module also provides the Thread class, which represents a thread of control
