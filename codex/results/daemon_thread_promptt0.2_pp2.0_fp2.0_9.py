import threading
# Test threading daemon

def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=test_daemon)
    d.setDaemon(True)

    d.start()
    d.join()
    print('main thread')

# Test threading lock

import threading

class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value = value = self.value + 1
        self.lock.release()
        return value

# Test threading condition

import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.
