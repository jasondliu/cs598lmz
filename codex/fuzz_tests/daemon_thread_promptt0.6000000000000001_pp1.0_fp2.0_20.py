import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):
        while self._running:
            print("Thread is running")
            time.sleep(0.5)
            

my_thread = MyThread()
my_thread.start()
time.sleep(3)
my_thread.terminate()

print("End of main thread")

# Test threading with multiple threads

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        for i in range(self.counter):
            print("Thread: {}, Count: {}".format(self.name, i))
        
thread
