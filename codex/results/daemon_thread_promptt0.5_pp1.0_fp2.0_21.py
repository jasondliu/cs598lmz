import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))
        time.sleep(1)
        print("{} finished!".format(self.getName()))

for x in range(4):
    mythread = MyThread(name = "Thread-{}".format(x + 1))
    mythread.setDaemon(True)
    mythread.start()
    time.sleep(.9)

print("All done!")

# Test threading lock
class Box(object):
    lock = threading.RLock()
    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)

