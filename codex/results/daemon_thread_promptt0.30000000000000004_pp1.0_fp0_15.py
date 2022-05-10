import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.stop = False
    def run(self):
        while not self.stop:
            print("Thread %s" % self.name)
            time.sleep(self.delay)
    def stop(self):
        self.stop = True

t1 = MyThread("t1", 1)
t2 = MyThread("t2", 2)
t1.start()
t2.start()
time.sleep(10)
t1.stop()
t2.stop()

# Test threading lock

class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0
    def increment(self):
        self.lock.acquire()
        self.value = value = self.value + 1
        self.lock.release()
        return value

class Worker(threading.
