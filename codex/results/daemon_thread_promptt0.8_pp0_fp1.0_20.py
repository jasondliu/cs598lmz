import threading
# Test threading daemon
def test_threading_daemon():
    def test_func(name):
        while True:
            print('hello ', name)
            time.sleep(1)

    thread = threading.Thread(target=test_func, args=('xxx',), daemon=True)
    thread.start()
    time.sleep(10)

# Test threading with lock
def test_threading_with_lock():
    class Share(object):
        def __init__(self):
            self.val = 0
            self.lock = threading.Lock()
        def add(self, delta):
            with self.lock:
                self.val += delta
                return self.val

    share = Share()
    def work(id):
        count = 1000000
        for i in range(count):
            share.add(1)
        print('thread {} finish add {}'.format(id, count))

    n = 10
    threads = []
    for i in range(n):
        thread = threading.Thread(target=work, args=(i,))
        threads.append(
