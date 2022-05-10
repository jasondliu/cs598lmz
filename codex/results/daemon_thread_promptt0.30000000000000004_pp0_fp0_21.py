import threading
# Test threading daemon
import time
import sys
import os
import signal

# Test threading daemon
import time
import sys
import os
import signal

class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.running = True
        self.count = 0
        print("Thread %s started" % self.name)

    def run(self):
        while self.running:
            self.count += 1
            print("Thread %s running %d" % (self.name, self.count))
            time.sleep(1)

    def stop(self):
        self.running = False
        print("Thread %s stopped" % self.name)


def handler(signum, frame):
    print("Signal handler called with signal", signum)
    print("Thread %s stopped" % thread.name)
    thread.stop()
    sys.exit(0)


if __name__ == "__main__":
    thread = TestThread("Test")
    thread.
