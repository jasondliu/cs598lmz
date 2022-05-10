import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Get a list of all active threads
import threading
threading.enumerate()

# Sample of using queues
from queue import Queue
queue = Queue()

def consumer():
  print('Consumer waiting')
  queue.get()  # Runs after put() below
  print('Consumer done')

threading.Thread(target=consumer).start()

print('Producer putting')
queue.put(object())  # Runs before get() above
print('Producer done')
