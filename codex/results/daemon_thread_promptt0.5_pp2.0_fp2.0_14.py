import threading
# Test threading daemon

def my_func(i):
    print("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    print("finished sleeping from thread %d" % i)

for i in range(10):
    t = threading.Thread(target=my_func, args=(i,))
    t.setDaemon(True)
    t.start()

print("done")

# Test threading in python

import threading
import time

def my_func(i):
    print("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    print("finished sleeping from thread %d" % i)

for i in range(10):
    t = threading.Thread(target=my_func, args=(i,))
    t.start()

print("done")

# Test threading in python

import threading
import time

def my_func(i):
    print("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    print("finished
