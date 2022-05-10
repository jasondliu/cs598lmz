import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()
        
        for i in range(100):
            mutex.acquire()
            count = count + 1
            mutex.release()
            
            print("{0} {1}: {2}".format(threadname, self.name, count))
            
        print("{0} {1} finished".format(threadname, self.name))
        
mutex = threading.Lock()
count = 0

thread1 = MyThread("A")
thread2 = MyThread("B")
thread1.start()
thread2.start()

print("Main thread end")

# Test threading lock

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name
