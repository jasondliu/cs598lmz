import threading
# Test threading daemon
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global counter, mutex
        time.sleep(1)
        if mutex.acquire(1):
            counter += 1
            print('I am %s, set counter:%s' % (self.name, counter))
            mutex.release()

counter = 0
mutex = threading.Lock()

for i in range(10):
    my_thread = MyThread(str(i))
    my_thread.start()

print('Main thread exit!')
