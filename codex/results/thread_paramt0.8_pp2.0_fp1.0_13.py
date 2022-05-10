import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hello')).start()

#Hello, world! 5
#Hello, world! 7
#Hello, world! 9
#Hello, world! 11

#Hello, world! 13
#Hello, world! 15
#Hello, world! 17
#helloHello, world! 19
#Hello, world! 21
#Hello, world! 23
#Hello, world! 25
distributed_lock_on_a_shared_resource_with_threads

import threading
import time
class SharedCounter(object):
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta

counters = SharedCounter()

#to do some
def worker(delta):
    for i in range(10):
        time.sleep(0
