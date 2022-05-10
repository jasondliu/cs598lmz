import threading
# Test threading daemon thread, single thread with multiple sub-threads

# In Python, a class can be made into a thread by extending the Thread class
# and overriding the run() method.
class MyThread(threading.Thread):
    def __init__(self, n, sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print("Thread started.")
        print("Sleep for %d sec." % self.sleep_time)
        time.sleep(self.sleep_time)
        print("Thread done.")

# Create a new thread
thread = MyThread(1, 5)
thread.start()

# Wait for the thread to complete
thread.join()

# Create new threads
threads = []
threads += [MyThread(i, i) for i in range(5)]

# Start threads
for i in threads:
    i.start()

# Wait for all threads to complete
for i in threads:
    i.join()
