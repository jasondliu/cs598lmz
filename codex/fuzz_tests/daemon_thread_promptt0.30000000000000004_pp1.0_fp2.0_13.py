import threading
# Test threading daemon
import time

def daemon():
    print('Start:', threading.current_thread().name)
    time.sleep(2)
    print('End:', threading.current_thread().name)

def non_daemon():
    print('Start:', threading.current_thread().name)
    print('End:', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# d.join()
# t.join()

# print('End of program.')

# Test threading lock
import threading
import time

class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add
