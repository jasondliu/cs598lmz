import threading
# Test threading daemon

data=[]

class Task(threading.Thread):
    def __init__(self,lock,data):
        self.lock = lock
        self.data = data
        super(Task,self).__init__()

    def run(self):
        self.lock.acquire()
        self.data.append(1)
        self.lock.release()


threads = []
lock = threading.Lock()
for j in range(100):
    for i in range(100):
        t = Task(lock,data)
        t.start()
        threads.append(t)
    print("100 done")
    time.sleep(0.001)

for t in threads:
    t.join()

print("All done")
print(len(data))

#print("Number of thread: %d" % threading.active_count())
#print("Threads: {}".format(threading.enumerate()))

print("Current thread: {}".format(threading.current_thread()))
print("Current thread: {}".format(thread
