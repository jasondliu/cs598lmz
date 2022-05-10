import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global counter, mutex
        time.sleep(1)
        if mutex.acquire(1):
            counter += 1
            print('I am %s, set counter:%s' % (self.name, counter))
            mutex.release()
        time.sleep(1)

# Create mutex
mutex = threading.Lock()
# Create threads
threads = []
for i in range(5):
    threads.append(MyThread('thread-' + str(i)))

# Start threads
for i in range(5):
    threads[i].start()

# Wait for all threads to complete
for i in range(5):
    threads[i].join()

print('Main thread exiting.')

# Test threading lock
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__
