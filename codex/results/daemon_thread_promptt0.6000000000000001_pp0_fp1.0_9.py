import threading
# Test threading daemon mode
def daemon():
    print("Starting Daemon")
    time.sleep(1)
    print("Ending Daemon")

if __name__ == "__main__":
    # Set thread daemon mode to true
    d = threading.Thread(name="daemon", target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()
    print("End")

# Test threading lock
'''
import time
import threading

class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

def adder(box
