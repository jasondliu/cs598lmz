import threading
# Test threading daemon
# https://stackoverflow.com/questions/190010/daemon-threads-explanation

def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting :', threading.currentThread().getName())

def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting :', threading.currentThread().getName())

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# https://stackoverflow.com/questions/190010/daemon-threads-explanation
# https://docs.python.org/3/library/threading.html#threading.Thread.setDaemon
# https://docs.python.org/3/library/threading.html
