import threading
# Test threading daemon
class TaskThread(threading.Thread): 
    def run(self): 
        time.sleep(10)
        print('done with threading')
thr = TaskThread() 
thr.setDaemon(True) 
thr.start() 
 
# Do something during 10 second...
time.sleep(5)
print('done with main')
# Test threading daemon

import random
import time
from threading import Thread

temp = {}
def put():
    for i in range(100000):
        temp[i] = random.random() * 10000000
    print("put done")
def get():
    for i in range(100000):
        x = temp[i]

t1 = Thread(target=put)
t2 = Thread(target=get)
t1.start()
t2.start()

print("done with main")
import threading

def print_cube(num):
    print("Cube: {}".format(num * num * num) + "\n")
    print("Thread terminates")

def print_square(
