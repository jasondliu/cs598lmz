import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none
# https://docs.python.org/2/library/threading.html
# https://docs.python.org/2/library/thread.html
# http://www.bogotobogo.com/python/Multithread/python_multithreading_subclassing_daemon_thread.php

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
    
    def run(self):
        print("Thread starting...")
        x = 0
        while True:
            x += 1
            print("Thread running...")
            time.sleep(1)

thread = MyThread()
thread.start()

time.sleep(5)
print("Main thread ending...")

# Output:
# Thread starting...
# Thread running...
# Thread running...
# Thread running...
# Thread running...
# Main thread ending...
# Thread
