import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
    def run(self):
        print "Thread %s started" % self.name
        time.sleep(3)
        print "Thread %s finished" % self.name

th1 = MyThread("th1")
th2 = MyThread("th2")
th1.start()
th2.start()
time.sleep(1)
print "Main thread finished"

# Test threading lock

class MyThread(threading.Thread):
    def __init__(self, name, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.lock = lock
    def run(self):
        self.lock.acquire()
        print "Thread %s started" % self.name
        time.sleep(3)
        print "Thread %s finished" % self.name
        self.lock.release()


