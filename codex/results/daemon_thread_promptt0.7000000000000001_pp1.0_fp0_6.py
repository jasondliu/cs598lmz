import threading
# Test threading daemon
import time

def worker() :
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(1)
    print(threading.current_thread().getName(), 'Exiting')

def my_service() :
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# t.join()
# w.join()
# w2.join()

# Test threading.Lock
import threading
import time

class Counter(object) :
    def __init__(self) :
        self.lock = threading.Lock()
        self.value = 0

    def increment(self) :
        self
