import threading
# Test threading daemon
def test_threading_daemon():
    def worker():
        print('Worker')
        return

    thread = threading.Thread(target=worker)
    thread.setDaemon(True)
    thread.start()
    thread.join()

# Test threading
def test_threading():
    def worker():
        print('Worker')
        return

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()

# Test threading with args
def test_threading_args():
    def worker(num):
        print('Worker: %s' % num)
        return

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

# Test threading with kwargs
def test_threading_kwargs():
    def worker(num):
        print('Worker: %s' % num)
        return

    threads = []
    for i in range(5):
