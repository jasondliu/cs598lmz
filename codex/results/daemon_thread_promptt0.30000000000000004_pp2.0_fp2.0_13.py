import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            print(self.name)
            time.sleep(1)

t1 = MyThread('t1')
t2 = MyThread('t2')

time.sleep(5)

print('Done')

# Test threading with queue

class MyThread(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            msg = self.queue.get()
            print(self.name, msg)
            time.sleep(1)

queue = queue.Queue()

t1 = MyThread('t1', queue
