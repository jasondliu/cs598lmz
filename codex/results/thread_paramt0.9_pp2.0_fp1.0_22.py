import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# Asynchronous I/O and Event-Driven Programming
# Python's other synchronization tool - the condition variable
# Condition variable requires two methods to be called in a specific order
# 1. wait - waits for a condition variable to be true. The condition variable is locked until the wait method releases it
# 2. notify - unblock at most one thread which is waiting to be notified
# A condition variable is intended to be used by multiple threads
# It is the basis of a higher-level of synchronization tool - thread-safe queues (data structure that allows multiple threads to access the same object safely)

# condition variable is built on top of a lock, which is an internal lock
# The lock can be accessed as _lock.
import threading, time
class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start
