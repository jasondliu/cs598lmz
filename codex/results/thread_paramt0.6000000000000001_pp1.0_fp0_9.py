import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Output:
# Hello from thread 2
# Hello from thread 1

# The reason for this is that the CPython interpreter is not thread-safe, and therefore it is not safe to use
# print in multiple threads at the same time. This is true even if you print to a file, or use a lock around the
# print statement.

# The reason for this limitation is that print is not an atomic operation in CPython.
# The implementation of print in CPython has to acquire a lock, then it does the actual printing,
# then it releases the lock. If multiple threads are calling print at the same time,
# then the lock will prevent them from doing the printing at the same time, but it won't prevent the threads
# from acquiring the lock and getting to the point where they are about to do the printing at the same time.
# When that happens, you get the output interleaved like in our example.

# The print function in
