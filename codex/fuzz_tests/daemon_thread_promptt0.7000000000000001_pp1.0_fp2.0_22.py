import threading
# Test threading daemon
def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
def non_daemon():
    print('Starting')
    print('Exiting')
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()

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
    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()
    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()
def adder
