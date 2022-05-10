import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('End daemon')

def non_daemon():
    print('Start non_daemon')
    print('End non_daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

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
do_with_lock(lock)
lock.release()
print('Lock is released')

# Test threading condition
condition = threading.Condition()
def consumer(condition):
    with condition:
        print('Consumer before wait')
        condition.wait()
        print('Consumer after wait')

def producer(condition):

