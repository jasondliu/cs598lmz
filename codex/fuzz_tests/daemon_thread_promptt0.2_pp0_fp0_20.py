import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:', threading.currentThread().getName())
        time.sleep(2)
        print('Exiting :', threading.currentThread().getName())

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    def non_daemon():
        print('Starting:', threading.currentThread().getName())
        print('Exiting :', threading.currentThread().getName())

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()

# Test threading join
def test_threading_join():
    def worker():
        """thread worker function"""
        print('Worker')
        return

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

#
