import threading
# Test threading daemon
import time

class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True

    def run(self):
        while True:
            print('Thread %s is running' % self.name)
            time.sleep(1)

def test_thread():
    t1 = TestThread('1')
    t2 = TestThread('2')
    t1.start()
    t2.start()
    time.sleep(3)
    print('main thread exit')

# test_thread()

# Test threading lock
import threading
import time

class TestThread(threading.Thread):
    def __init__(self, name, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print('Thread %s is running' % self.name)
        time.sleep(1)
