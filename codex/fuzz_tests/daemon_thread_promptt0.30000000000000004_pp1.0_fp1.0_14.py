import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print("Hello")
            time.sleep(1)

MyThread()
time.sleep(10)
print("Bye")

# Test threading with args

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.start()

    def run(self):
        print("Hello", self.name)

MyThread("World")

# Test threading with args and daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print("Hello", self
