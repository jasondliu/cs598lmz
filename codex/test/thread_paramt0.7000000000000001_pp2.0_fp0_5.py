import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

import time, random
def compute():
    for i in range(10):
        time.sleep(0.1)
        print(random.random())
compute()

threading.Thread(target=compute).start()
threading.Thread(target=compute).start()

t1 = threading.Thread(target=compute)
t2 = threading.Thread(target=compute)
t1.start()
t2.start()
t1.join()
t2.join()

import time, threading, random

class Compute(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
    def run(self):
        for i in range(10):
            time.sleep(0.1)
            print(random.random())

