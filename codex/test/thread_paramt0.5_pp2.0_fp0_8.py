import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Hello from thread 1
# Hello from thread 2

# Threads share global memory by default.
# To avoid race conditions, use a Lock object.
# A Lock is like a light switch: it can be either on or off.
# If the lock is on, only one thread can execute the code at a time.
# If the lock is off, any number of threads can execute the code.
# When you want to execute some code, you turn the lock on,
# execute the code, and then turn the lock off.

# To turn the lock on, call the acquire method.
# To turn the lock off, call the release method.

# If multiple threads try to acquire a lock that's already on,
# they are put into a queue and wait their turn.
# If a thread tries to release a lock that's already off,
# a RuntimeError is raised.

import threading, time
