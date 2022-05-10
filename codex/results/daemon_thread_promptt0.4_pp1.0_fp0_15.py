import threading
# Test threading daemon
class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()
        for i in range(100000):
            mutex.acquire()
            count = count + 1
            mutex.release()
        print threadname, count

count = 0
mutex = threading.Lock()
threads = []
for i in range(5):
    threads.append(TestThread("thread-"+str(i)))

for t in threads:
    t.setDaemon(True)
    t.start()

for t in threads:
    t.join()

print "main thread:", count
