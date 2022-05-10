import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(target=test_daemon, daemon=True)
d.start()
print('main thread')

# Test threading lock
lock = threading.Lock()
def test_lock():
    if lock.acquire():
        print('lock acquired')
        time.sleep(2)
        lock.release()
        print('lock released')

t = threading.Thread(target=test_lock)
t.start()
print('main thread')

# Test threading with queue
q = queue.Queue()
def test_queue():
    for i in range(10):
        q.put(i)
    print('put finished')

t = threading.Thread(target=test_queue)
t.start()
while not q.empty():
    print(q.get())
print('get finished')

# Test threading with queue
q = queue.Queue()
def test_queue():
    for i in range(10
