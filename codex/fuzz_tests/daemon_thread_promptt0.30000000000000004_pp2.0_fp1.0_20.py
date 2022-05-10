import threading
# Test threading daemon
def thread_test():
    print("Start threading")
    time.sleep(2)
    print("End threading")

thread = threading.Thread(target=thread_test)
thread.setDaemon(True)
thread.start()

print("Main threading")

# Test threading daemon

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print("Start threading: " + self.name)
        time.sleep(2)
        print("End threading: " + self.name)

thread = MyThread("MyThread")
thread.setDaemon(True)
thread.start()

print("Main threading")

# Test threading daemon
