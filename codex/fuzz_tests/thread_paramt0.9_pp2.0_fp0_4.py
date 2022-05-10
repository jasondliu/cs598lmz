import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 1\n')).start()
print 'Hello from\nMain Thread'

#using daemon threads
import threading, time

def sleeper(i):
    print 'thread %d sleeps for 5 seconds' % i
    time.sleep(5)
    print 'thread %d woke up' % i

for i in range(10):
    t = threading.Thread(target=sleeper, args=(i,))
    t.setDaemon(True)
    t.start()
from threading import Thread, Lock
i = 0
lock = Lock()

def adder():
    global i
    lock.acquire()
    i += 1
    lock.release()

threads = []
for n in xrange(100):
    t = Thread(target=adder)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print i

from threading import Thread, Lock
i = 0
lock = Lock()

def adder():
    global i
