import select
# Test select.select function
import time

SLEEP_TIME = 1

def slow_syscall():
    select.select([], [], [], SLEEP_TIME)

start = time.time()
for _ in range(5):
    slow_syscall()
end = time.time()
print("Took %.3f seconds" % (end - start))

# Context manager for a single thread
from threading import Thread

class MyThread(Thread):
    def __init__(self, event):
        self.event = event
        super().__init__()

    def run(self):
        print("MyThread waiting for the event")
        event_is_set = self.event.wait()
        print("event set: %s" % event_is_set)

e = threading.Event()
t = MyThread(e)
t.start()

print("MainThread waiting before calling Event.set()")
time.sleep(0.1)
e.set()
print("Event is set")

# Context manager for a thread pool
import concurrent.fut
