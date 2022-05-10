import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('exit')

if __name__ == '__main__':
    d = threading.Thread(name='test_daemon', target=test_daemon)
    d.setDaemon(True)
    d.start()
    d.join()
    print('main thread')

# Test threading queue
import queue
q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()

# Test threading lock
lock = threading.Lock()
total = 0
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()
def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()
threads = []
t1 =
