import threading
# Test threading daemon
import threading

class TestThreading(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("Starting " + str(self.threadID))
        print("Exiting " + str(self.threadID))

# Create new threads
thread1 = TestThreading(1)
thread2 = TestThreading(2)

# Start threads
thread1.start()
thread2.start()

print("Exiting main thread")

# run exection time
start_time = time.time()

#----------------------------------

# YOUR CODE GOES HERE

#----------------------------------

print("My program took "+ str(time.time() - start_time) + " to run")
