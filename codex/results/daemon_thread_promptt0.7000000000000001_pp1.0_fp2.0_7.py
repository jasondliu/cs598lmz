import threading
# Test threading daemon=True

class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.1):
            print(threading.currentThread().getName())


stopFlag = threading.Event()
threads = [MyThread(stopFlag) for i in range(10)]

for t in threads:
    t.start()

import time
time.sleep(5)

stopFlag.set()

for t in threads:
    t.join()
</code>

