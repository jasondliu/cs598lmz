import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(2)
    print('End')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start')
    print('End')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading lock
import threading

class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        try:
            self.value = self.value + 1
        finally:
            self.lock.release()

c = Counter()
for i in range(2):
    t = threading.Thread(target=c.increment)
    t.start()

print('Final value:', c.value)

# Test threading condition
import threading
import time
