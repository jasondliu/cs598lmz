import threading
# Test threading daemon
#
#
#
#
#

# The worker thread pulls an item from the queue and processes it
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()


# Create the queue and thread pool.
q = Queue.Queue()
for i in range(num_worker_threads):
     t = threading.Thread(target=worker)
     # t.setDaemon(True)
     t.start()

# stuff work items on the queue (in this case, just a number).
for item in source():
    q.put(item)

# Wait for all wo
