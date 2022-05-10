import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Threads share global memory space with the main thread.
# A lock is a synchronization primitive.
# It is commonly used to protect shared data from being simultaneously accessed by multiple threads.
# Locks are not owned by the threads that use them.
# A thread acquires a lock by calling its acquire() method.
# The thread then has access to the protected code.
# When the thread no longer needs the lock, it can release it by calling the release() method.
# A thread can acquire a lock multiple times.
# When the lock has been acquired the same number of times as it has been released,
# it is unlocked and other threads can acquire it.
# If a thread attempts to release a lock that it does not own, a RuntimeError will be raised.

import threading
lock = threading.Lock()
lock.acquire()
