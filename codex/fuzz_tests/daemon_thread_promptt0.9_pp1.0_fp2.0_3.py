import threading
# Test threading daemon functionalities
class MyThread(threading.Thread):
    def __init__(self,index):
        self.index = index
        super(MyThread, self).__init__()

    def run(self):
        while True:
            print("Thread %d"%self.index)
            time.sleep(1)


# Create 6 threads
threads = []
for i in range(0,6):
    threads.append(MyThread(i))

# Start all threads
for t in threads:
    t.start()

# Join all threads
for t in threads:
    t.join()

# Check daemon status
for t in threads:
    print("thread %d is daemon: %s"%(t.index, t.isDaemon()))
