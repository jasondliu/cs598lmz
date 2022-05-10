import threading
# Test threading daemon

def test_thread():
    print('thread start')
    time.sleep(3)
    print('thread end')

t = threading.Thread(target=test_thread)
t.setDaemon(True)
t.start()

print('main thread')

# Test threading event

def test_event():
    print('event start')
    time.sleep(3)
    print('event end')

e = threading.Event()

t = threading.Thread(target=test_event)
t.start()

e.wait(timeout=1)
print('main thread')

# Test threading lock

def test_lock():
    print('lock start')
    time.sleep(3)
    print('lock end')

l = threading.Lock()

t = threading.Thread(target=test_lock)
t.start()

l.acquire()
print('main thread')
l.release()

# Test threading rlock

def test_rlock():
    print('rlock start')
    time
