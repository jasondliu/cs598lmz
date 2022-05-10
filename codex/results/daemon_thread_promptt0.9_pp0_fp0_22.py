import threading
# Test threading daemon.
def f1():
    print("f1 Starting")
    time.sleep(2)
    print("f1 End")

t = threading.Thread(target=f1)
t.daemon = True
t.start()
time.sleep(1)
print("Quitting")

# 5.3 Queue
# The Queue module has been renamed to queue in Python 3.
"""
import queue 
q = queue.Queue()
q.put("hi")
q.put("there")
q.put("you")
while not q.empty():
    print(q.get())
"""
# 5.4 Section Summary
# Python's threads can run in parallel. Reduce use of GIL and use as much I/O-bound 
# tasks as possible in threads.
# Use print and logging for debugging in multithreading. Do not use print function
# for real-time logging.
# Pool enables us to create a group of workers to run tasks in parallel. 
# Queue is a thread-safe data structure that can be used to share data between threads.
# Multithreading Programming Chapter 6
