import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()
        for x in xrange(0, 100000):
            mutex.acquire()
            count = count + 1
            mutex.release()
        print "thread %s finished" % threadname

# Test threading
def test_threading():
    global count, mutex
    threads = []
    count = 0
    mutex = threading.Lock()
    for x in xrange(0, 10):
        threads.append(MyThread(x))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print "all threads finished, count = %d" % count

# Test process
def test_process():
    global count
    count = 0
    for x in xrange(0, 10):
        p =
