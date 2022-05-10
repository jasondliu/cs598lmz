import threading
# Test threading daemon thread
def worker_daemon():
    print('Starting thread')
    time.sleep(2)
    print('Exiting thread')

def worker_non_daemon():
    print('Starting thread')
    time.sleep(2)
    print('Exiting thread')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=worker_daemon)
    d.setDaemon(True)
    t = threading.Thread(name='non-daemon', target=worker_non_daemon)
    d.start()
    t.start()
    d.join()
    t.join()
