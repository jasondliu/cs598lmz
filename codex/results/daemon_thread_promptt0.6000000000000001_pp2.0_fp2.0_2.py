import threading
# Test threading daemon
def foo(name):
    for i in range(4):
        print name, i
        time.sleep(1)
    print name, "done"

t1 = threading.Thread(target=foo, args=("Thread 1",))
t2 = threading.Thread(target=foo, args=("Thread 2",))
t3 = threading.Thread(target=foo, args=("Thread 3",))
t1.start()
t2.start()
t3.start()
# t1.join()
# t2.join()
# t3.join()



# Test threading with queue
class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.q = Queue.Queue()

    def enqueue(self, func, *args):
        self.q.put((func, args))

    def start(self):
        for i in range(self.num_threads):
            t = threading.Thread(target=self.
