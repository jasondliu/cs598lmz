import threading
# Test threading daemon
from time import sleep
from datetime import datetime

class TxThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            print('{}: {}'.format(datetime.now(), self.name))
            sleep(1)

t = TxThread()
t.start()
print('{}: {}'.format(datetime.now(), t.name))

# Check thread status
print(t.is_alive())

# Wait for thread to terminate
t.join()

# Terminate thread
t.join(1)

# Check thread status
print(t.is_alive())

sleep(10)

# ------------------------------------------------------------------------------
# Threading Lock
# ------------------------------------------------------------------------------

# Init thread lock
lock = threading.Lock()

# Acquire thread lock
lock.acquire()

# Release thread lock
lock.release()

# ------------------------------------------------------------------------------
# Threading Semaphore
# ------------------------------------------------------------------------------


