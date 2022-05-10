import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join()
t.join()

# Test threading locks
# https://docs.python.org/3/library/threading.html#lock-objects

class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        # self.lock.acquire()
        self.value = value = self.value + 1
        # self.
