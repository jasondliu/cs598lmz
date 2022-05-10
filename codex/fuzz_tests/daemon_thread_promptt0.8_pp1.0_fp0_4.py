import threading
# Test threading daemon
import time

class MyThread(threading.Thread):
    def __init__(self, val, sleep=0):
        super(MyThread, self).__init__()
        self.val = val
        self.sleep = sleep

    def run(self):
        if self.sleep > 0:
            time.sleep(self.sleep)
        print("thread completed: {}".format(self.val))

# Create the thread
try:
    t = MyThread("abc", 2)

    # Let the thread work
    t.start()

    # Do some other work
    print("some other work")
    time.sleep(1)

    # Wait for the thread to complete
    t.join()

    # Indicate that the thread is finished
    print("thread completed")

# Set up an exception if the thread finishes abruptly
except Exception as e:
    print("Exception: {}".format(e))

# End the script
print("done")

# Threading daemon in Python

# Import the threading module
import threading
# Test threading daemon
import time

