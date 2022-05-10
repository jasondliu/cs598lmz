import threading
# Test threading daemon
class TestThread(threading.Thread):
    def __init__(self, name, msg):
        threading.Thread.__init__(self)
        self.name = name
        self.msg = msg
    def run(self):
        print("Starting thread: ", self.name)
        prt(self.msg, 3)
        print("Exiting thread: ", self.name)

def threading_test():
    thread1 = TestThread("Thread1", "Testing threading!")
    thread2 = TestThread("Thread2", "Testing double threading!")
    thread1.start()
    thread2.start()

# threading_test()
