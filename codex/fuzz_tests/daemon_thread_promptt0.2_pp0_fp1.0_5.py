import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name
    
    def run(self):
        print("Thread %s is running" % self.name)
        time.sleep(1)
        print("Thread %s is ended" % self.name)

if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main thread is ended")

# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name
    
    def run(self):
        print("Thread %s is running" % self.name)
        time.sleep(1)
        print("Thread %s is ended" % self.name)
