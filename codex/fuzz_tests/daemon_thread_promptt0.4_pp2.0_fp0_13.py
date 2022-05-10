import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('stop')

for i in range(5):
    t = threading.Thread(target=test_daemon)
    t.setDaemon(True) # set daemon so main thread can exit when receives ctrl-c
    t.start()

t.join()
print('main_thread_exit')

# Test threading join
def test_join(x):
    print('start', x)
    time.sleep(2)
    print('stop', x)

for i in range(5):
    t = threading.Thread(target=test_join, args=(i,))
    t.start()
    t.join()

print('main_thread_exit')

# Test threading lock
lock = threading.Lock()

def test_lock(x):
    lock.acquire()
    print('start', x)
    time.sleep(2)
    print('stop', x)
    lock.release()

for i in range(5
