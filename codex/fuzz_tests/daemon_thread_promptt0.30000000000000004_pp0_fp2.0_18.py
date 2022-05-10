import threading
# Test threading daemon

def worker():
    print "I am working"
    time.sleep(1)
    print "I am done"

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print "Main thread is done"

# Test threading lock

lock = threading.Lock()

def worker2():
    lock.acquire()
    print "I am working"
    time.sleep(1)
    print "I am done"
    lock.release()

threads2 = []
for i in range(5):
    t = threading.Thread(target=worker2)
    threads2.append(t)
    t.start()

print "Main thread is done"

# Test threading condition

condition = threading.Condition()

def worker3():
    condition.acquire()
    print "I am working"
    time.sleep(1)
    print "I am done"
    condition.
