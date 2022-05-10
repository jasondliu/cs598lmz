import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Thread %s is running"%(self.name))
        time.sleep(1)

if __name__ == "__main__":
    t1 = MyThread("Thread-1")
    t2 = MyThread("Thread-2")
    t1.start()
    t2.start()
    print("Main thread")

# Test threading lock
lock = threading.Lock()
class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        lock.acquire()
        print("Thread %s is running"%(self.name))
        time.sleep(1)
        lock.release()

if __name__ == "__main__":
    t1 = MyThread("Thread-1")
    t
