import threading
# Test threading daemon

def worker():
  print("Worker")
  return

threads = []
for i in range(5):
  t = threading.Thread(target=worker)
  #t.daemon = True
  threads.append(t)
  t.start()

for t in threads:
  t.join()

print("Done")

# Test threading with queue
import queue
import threading
import time

def worker(q):
  while True:
    item = q.get()
    print("Worker", item)
    time.sleep(1)
    q.task_done()

q = queue.Queue()

threads = []
for i in range(5):
  t = threading.Thread(target=worker, args=(q,))
  #t.daemon = True
  threads.append(t)
  t.start()

for i in range(20):
  q.put(i)

q.join()

print("Done")

# Test threading with queue
import queue
import threading
import
