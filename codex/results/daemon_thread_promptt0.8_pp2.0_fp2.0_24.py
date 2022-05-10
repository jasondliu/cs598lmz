import threading
# Test threading daemon
def daemon():
    print('Starting')
    time.sleep(2)
    print('Exiting')

# Test non-daemon thread
def non_daemon():
    print('Starting')
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon',target=non_daemon)

d.start()
t.start()

t.join()

d.join()
