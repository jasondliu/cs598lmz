import threading
# Test threading daemon mode

# def worker():
#     print('I am thread')
#     t = threading.currentThread()
#     time.sleep(10)
#     print(t.getName(), 'Exiting...')

# new_t = threading.Thread(target=worker, name='Worker')
# new_t.setDaemon(True)
# new_t.start()
# new_t.join(2)
# print('Main thread exiting...')


# Test threading lock

def worker(s, lock):
    # lock.acquire()
    with lock:
        print('I am thread')
        t = threading.currentThread()
        time.sleep(10)
        print(t.getName(), 'Exiting...')
        s.release()

lock = threading.Lock()
# lock.acquire()
s = threading.Semaphore(3)
new_t = threading.Thread(target=worker, args=(s,lock), name='Worker')
new_t.start()

new_t = threading.Thread
