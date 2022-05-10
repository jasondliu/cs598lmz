import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print("Exiting main thread")

# Test threading lock
lock = threading.Lock()

def thread_1():
    print("Thread 1 Waiting for lock")
    with lock:
        print("Thread 1 Acquired lock")

def thread_2():
    print("Thread 2 Waiting for lock")
    with lock:
        print("Thread 2 Acquired lock")

t1 = threading.Thread(target=thread_
