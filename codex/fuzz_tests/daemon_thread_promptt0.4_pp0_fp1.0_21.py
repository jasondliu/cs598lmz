import threading
# Test threading daemon
def test():
    while True:
        print('test')
        time.sleep(1)

t = threading.Thread(target=test)
t.setDaemon(True)
t.start()

# Test threading lock
lock = threading.Lock()

def test2():
    print('test2')
    lock.acquire()
    print('test2 get lock')
    time.sleep(5)
    lock.release()
    print('test2 release lock')

t2 = threading.Thread(target=test2)
t2.start()

time.sleep(1)

lock.acquire()
print('main get lock')
lock.release()
print('main release lock')

# Test threading event
event = threading.Event()

def test3():
    print('test3')
    event.wait()
    print('test3 get event')

t3 = threading.Thread(target=test3)
t3.start()

time.sleep(1)
event.set()
print('main set event')
