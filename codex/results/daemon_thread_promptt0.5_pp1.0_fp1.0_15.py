import threading
# Test threading daemon
import time
from datetime import datetime
from datetime import timedelta

from threading import Thread
from threading import Lock
import time
from datetime import datetime
from datetime import timedelta


class Task(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.running = True
        self.lock = Lock()
        self.lock.acquire()
        self.time = datetime.now()
        self.lock.release()

    def run(self):
        while self.running:
            with self.lock:
                self.time = datetime.now()
                print(self.name, self.time)
            time.sleep(1)

    def stop(self):
        self.running = False

    def get_time(self):
        with self.lock:
            return self.time


x = Task("x")
y = Task("y")

x.start()
y.start()

time.sleep(5)
x.stop()
y.stop
