import threading
# Test threading daemon
def daemon():
    print('Start:', threading.currentThread().getName())
    time.sleep(2)
    print('End:', threading.currentThread().getName())

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start:', threading.currentThread().getName())
    print('End:', threading.currentThread().getName())

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value = value = self.value + 1
        self.lock.release()
        return value

class LockingCounter(object):
    def __init__(self):
