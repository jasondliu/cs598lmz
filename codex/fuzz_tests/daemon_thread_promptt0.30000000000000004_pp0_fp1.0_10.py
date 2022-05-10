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

# d.join()
# t.join()

# Test threading lock
# lock = threading.Lock()
#
# def f():
#     with lock:
#         print(threading.current_thread().name)
#         time.sleep(1)
#         print(threading.current_thread().name)
#
# def g():
#     with lock:
#         print(threading.current_thread().name)
#         time.sleep(1)
