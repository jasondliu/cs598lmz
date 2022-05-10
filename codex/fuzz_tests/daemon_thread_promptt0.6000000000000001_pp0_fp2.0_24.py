import threading
# Test threading daemon
def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
    t.join()

print('Done')

# Test multiprocessing
import multiprocessing
import time

def worker(num):
    """thread worker function"""
    print('Worker:', num)
    time.sleep(5)

jobs = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    jobs.append(p)
    p.start()

for j in jobs:
    j.join()

print('Done')

# Test import
import sys
sys.path.append('/home/martin/Documents/Python/')
import fibo
print(fibo.fib(1000))

# Test os
import os
print(os.getcwd())
print(os.listdir('/
