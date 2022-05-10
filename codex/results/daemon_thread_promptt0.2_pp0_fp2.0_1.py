import threading
# Test threading daemon

def daemon():
    print('Start daemon')
    time.sleep(2)
    print('End daemon')

def non_daemon():
    print('Start non-daemon')
    print('End non-daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('End of program')

# Test threading lock

lock = threading.Lock()

def thread_1():
    print('Thread 1 start')
    lock.acquire()
    print('Thread 1 acquire lock')
    time.sleep(2)
    lock.release()
    print('Thread 1 release lock')
    print('Thread 1 end')

def thread_2():
    print('Thread 2 start')
    lock.acquire()
    print('Thread 2 acquire lock')
    time.sleep(2)
    lock
