import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)
def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)
if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=daemon, daemon=True)
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()

# Test threading lock
lock = threading.Lock()
def do_this(lock):
    lock.acquire()
    try:
        with open('text.txt', 'a') as f:
            f.write('Lock acquired via with\n')
    finally:
        lock.release()

def do_something_else(lock):
    lock.acquire()
    try:
        with open('text.txt
