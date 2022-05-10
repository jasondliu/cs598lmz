import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global num
        time.sleep(1)
        if lock.acquire():
            num += 1
            msg = self.name + ' set num to ' + str(num)
            print(msg)
            lock.release()

num = 0
lock = threading.Lock()
t_list = []

for i in range(5):
    t = MyThread('thread-' + str(i))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print('main thread stop!')

# Test threading

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global num
        time
