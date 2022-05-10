import threading
# Test threading daemon mode

def worker(fn, log, *args, **kwargs):
    f = open(log, 'a')
    f.write('Hi, this is a log\n')
    f.close()
    fn(*args, **kwargs)

def do_something(x, y=1):
    return x**y

def start_thread(fn, log, *args, **kwargs):
    thread = threading.Thread(target=worker, args=(fn, log) + args, kwargs=kwargs)
    thread.daemon = True
    thread.start()

start_thread(do_something, 'test1.log', 2, y=3)

while threading.active_count() > 1:
    time.sleep(1)
# Test threading

class TestThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter
    def run
