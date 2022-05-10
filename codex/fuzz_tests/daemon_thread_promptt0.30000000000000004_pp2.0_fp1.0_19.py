import threading
# Test threading daemon
def daemon():
    print('Start:', threading.current_thread().name)
    time.sleep(2)
    print('End:', threading.current_thread().name)

def non_daemon():
    print('Start:', threading.current_thread().name)
    print('End:', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('End of main thread')

# Test threading lock
lock = threading.Lock()

def print_square(num):
    lock.acquire()
    try:
        print(num**2)
    finally:
        lock.release()

threads = []
for i in range(10):
    t = threading.Thread(target=print_square, args=(i,))
    threads.append(t)

