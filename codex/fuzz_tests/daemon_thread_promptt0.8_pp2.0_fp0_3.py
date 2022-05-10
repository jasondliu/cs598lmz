import threading
# Test threading daemon
def run(*args):
    while True:
        print('Hello World!')
        time.sleep(0.5)
class Hello(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        while True:
            print("Hello", self.name)
            time.sleep(0.5)
if __name__ == '__main__':
    Hello("123").start()
    Hello("456").start()
    Hello("789").start()
    time.sleep(100)

import threading
from queue import Queue
from time import ctime
import time

def run(n, q):
    while True:
        print('Hello World!', n)
        time.sleep(0.5)
        if q.qsize() < 3:
            q.put(n)
        else:
            break

def main():
    q = Queue()
    t1 = threading.Thread(target=run, args=('123',q))
    t2
