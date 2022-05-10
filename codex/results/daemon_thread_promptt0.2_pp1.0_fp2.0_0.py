import threading
# Test threading daemon
# https://stackoverflow.com/questions/6920302/how-to-make-a-daemon-thread-in-python

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, 2)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = MyThread("Thread-1")
thread2 = MyThread("Thread-2")

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")

# https://stackoverflow.com/questions/6920302/how-to-make-
