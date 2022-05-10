import threading
threading.enumerate()

# Starting a thread
def sleeper(i):
    print("thread {} sleeps for 5 seconds".format(i))
    time.sleep(5)
    print("thread {} woke up".format(i))

for i in range(10):
    t = threading.Thread(target=sleeper, args=(i,))
    t.start()

# Shutting down threads gracefully
class CustomThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stopevent = threading.Event()
        self.daemon = True
    def run(self):
        while True:
            print("working...")
            time.sleep(1)
            if self._stopevent.is_set():
                print("done, shutting down...")
                return
    def stop(self):
        self._stopevent.set()

ex = CustomThread()
ex.start()
ex.stop()

# Monitoring workqueue jobs
import queue
def worker(q):
    while True:
        item
