import threading
# Test threading daemon

def func():
    print('func() passed to thread')

t = threading.Thread(target=func)
t.daemon = True
t.start()

# t.join()

print('Main thread exit')

# Test threading lock

lock = threading.Lock()

def func2():
    print('func2() passed to thread')
    lock.acquire()
    print('func2() got lock')
    lock.release()

t2 = threading.Thread(target=func2)
t2.start()
t2.join()

print('Main thread exit')

# Test threading event

event = threading.Event()

def func3():
    print('func3() passed to thread')
    event.wait()
    print('func3() recv event')

t3 = threading.Thread(target=func3)
t3.start()

print('Main thread waiting')
event.set()
print('Main thread set event')

t3.join()

print('Main thread exit')

#
