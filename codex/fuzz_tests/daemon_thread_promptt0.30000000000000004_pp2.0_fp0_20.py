import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
        self.start()

    def run(self):
        print("Starting thread: ", self.name)
        time.sleep(2)
        print("Exiting thread: ", self.name)

t1 = MyThread("t1")
t2 = MyThread("t2")
t3 = MyThread("t3")

print("Main thread exiting")

# Output:
# Starting thread:  t1
# Starting thread:  t2
# Starting thread:  t3
# Main thread exiting
# Exiting thread:  t1
# Exiting thread:  t2
# Exiting thread:  t3

# If we comment out the daemon property, then the main thread will wait for the child threads to finish before exiting.

# Starting thread:  t1
# Starting thread:  t2
# Starting thread:  t3
# Exiting thread:  t1
