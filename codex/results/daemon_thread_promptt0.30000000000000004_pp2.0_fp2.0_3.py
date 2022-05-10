import threading
# Test threading daemon
import time
import random

def worker():
    """thread worker function"""
    print 'Worker'
    time.sleep(random.randint(1,10))
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print "All threads started"
for t in threads:
    t.join()
print "All threads finished"

# Test threading daemon
import threading
import time
import random

def worker():
    """thread worker function"""
    print 'Worker'
    time.sleep(random.randint(1,10))
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print "All threads started"
for t in threads:
    t.join()
print "All threads finished"
