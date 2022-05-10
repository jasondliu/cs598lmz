import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('exit')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

def non_daemon():
    print('start')
    print('exit')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def test_lock():
    with lock:
        print('lock')
        time.sleep(2)

t1 = threading.Thread(name='lock', target=test_lock)
t2 = threading.Thread(name='lock', target=test_lock)

t1.start()
t2.start()

t1.join()
t2.join()

# Test threading condition
condition = threading.Condition()

def test_condition():
    with condition:

