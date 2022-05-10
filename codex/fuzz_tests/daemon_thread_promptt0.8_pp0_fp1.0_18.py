import threading
# Test threading daemon mode
class CountingThread(threading.Thread):
    def run(self):
        while True:
            print(threading.current_thread().getName())
            time.sleep(0.5)

CountingThread().start()
CountingThread().start()


# Test threading lock
lock = threading.Lock()
lock.acquire()
lock.release()

# Test threading queue
queue = queue.Queue()
queue.put(5)
queue.get()

# Test threading RLock
lock = threading.RLock()
lock.acquire()
lock.release()
