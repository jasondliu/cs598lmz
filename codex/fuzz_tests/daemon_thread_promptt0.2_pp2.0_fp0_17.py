import threading
# Test threading daemon
def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:')
    print('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

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
        thread = threading.Thread(target=func, args=args)
        threads.append
