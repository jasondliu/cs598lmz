import threading
# Test threading daemon thread
threading.current_thread().isDaemon()
import atexit
def thread_func():
    for i in range(20):
        print(threading.current_thread().name,i)
    atexit.register(thread_func)
    thread_func()
    print("Main function over..............")

# synchronized Lock
class Node():
    def __init__(self, value):
        self.value = value
    #@property
    def get_value(self):
        pass
    #@value.setter
    def set_value(self, value, password):
        pass

class Counter():
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        #self.lock.acquire()
        self.value += 1
        #self.lock.release()

# test Lock synchronizing
def func1():
    print("Function 1 starting......")
    with counter.lock:
        do_something()
        do_something_too()

def
