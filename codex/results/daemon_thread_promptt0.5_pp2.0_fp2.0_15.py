import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
    def run(self):
        for i in range(5):
            print(self.name, i)
            time.sleep(1)
        print(self.name, 'finished')

# Test threading join
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        for i in range(5):
            print(self.name, i)
            time.sleep(1)
        print(self.name, 'finished')

# Test threading lock
class MyThread(threading.Thread):
    def __init__(self, name, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.lock = lock
    def run(self):
        self.lock
