import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global stop_threads
        while not stop_threads:
            print(self.name)
            time.sleep(1)

stop_threads = False
thread1 = MyThread("Thread-1")
thread2 = MyThread("Thread-2")

thread1.start()
thread2.start()

time.sleep(5)
stop_threads = True

print("Exiting Main Thread")

# Test threading lock
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


