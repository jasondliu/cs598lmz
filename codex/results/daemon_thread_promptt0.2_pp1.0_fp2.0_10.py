import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html

def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Done')

# Test threading queue
# https://docs.python.org/3/library/queue.html

import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

# Test threading queue
# https://docs.python.org/3/library/queue.html

import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

# Test threading queue
# https://docs.python.org/3
