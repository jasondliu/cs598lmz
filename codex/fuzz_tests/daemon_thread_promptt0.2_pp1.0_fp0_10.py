import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('End daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non daemon')
    print('End non daemon')

t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def do_with_lock(lock):
    with lock:
        print('Lock is held')

lock.acquire()
print('Lock is held')
lock.release()
print('Lock released')

lock = threading.Lock()
first_thread = threading.Thread(target=do_with_lock, args=(lock,))
second_thread = threading.Thread(target=do_with_lock, args=(lock,))

first_thread.start()
second_thread.start
