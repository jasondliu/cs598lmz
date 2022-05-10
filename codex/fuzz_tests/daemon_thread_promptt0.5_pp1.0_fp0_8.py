import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        print('running with %s' % self.arg)
        time.sleep(1)

for i in range(5):
    t = MyThread(i)
    t.setDaemon(True)
    t.start()

print('main thread stop')

time.sleep(1)
print('main thread end')

# Test threading lock

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        counter.increment(1)

def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread
