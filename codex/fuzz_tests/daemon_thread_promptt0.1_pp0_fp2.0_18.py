import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

def non_daemon():
    print('start')
    print('end')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def test_lock():
    with lock:
        print('Lock is held')

t = threading.Thread(target=test_lock)
t.start()
t.join()

# Test threading event
event = threading.Event()

def waiter(event, n):
    print('{} waiting'.format(n))
    event_is_set = event.wait()
    print('event set: {}'.format(event_is_set))

def setter(event, n
