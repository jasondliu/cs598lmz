import threading
# Test threading daemon
def test_daemon():
    print('Start test_daemon')
    time.sleep(2)
    print('End test_daemon')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=test_daemon)
    d.setDaemon(True)
    d.start()
    d.join(1)
    print('d.isAlive()', d.isAlive())

# Test threading lock
lock = threading.Lock()
def test_lock():
    print('Start test_lock')
    lock.acquire()
    time.sleep(2)
    lock.release()
    print('End test_lock')

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=test_lock)
        t.start()

# Test threading condition
condition = threading.Condition()
products = 0

def producer(n):
    global products
    while True:
        if condition.acquire():
           
