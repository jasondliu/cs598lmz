import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-non-daemon-threads

class ThreadClass(threading.Thread):
    def run(self):
        for i in range(10):
            print(threading.current_thread().name)

t1 = ThreadClass()
t2 = ThreadClass()

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")

# Test threading lock
# https://www.tutorialspoint.com/python/python_multithreading.htm

threadLock = threading.Lock()
threads = []

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
