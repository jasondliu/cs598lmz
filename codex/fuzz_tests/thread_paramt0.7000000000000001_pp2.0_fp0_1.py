import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
"""

"""
from threading import Thread

print('hello')

def print_a():
    for i in range(100):
        print('A',end='')

def print_b():
    for i in range(100):
        print('B',end='')

thread1 = Thread(target=print_a)
thread2 = Thread(target=print_b)

thread1.start()
thread2.start()

print('bye')
"""

from threading import Thread
import time

class myThread(Thread):
    def __init__(self,name,sleepTime):
        super().__init__()
        self.name = name
        self.sleepTime = sleepTime

    def run(self):
        for i in range(100):
            print(self.name,end='')
            time.sleep(self.sleepTime)

thread1 = myThread('A',0.1)
thread1.start()

thread2 = myThread('B',0.2
