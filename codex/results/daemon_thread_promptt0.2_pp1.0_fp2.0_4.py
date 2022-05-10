import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('Exit daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non_daemon')
    print('Exit non_daemon')

t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
# lock = threading.Lock()
#
# def worker_with(lock):
#     with lock:
#         print(threading.current_thread().getName(), 'start')
#         time.sleep(2)
#         print(threading.current_thread().getName(), 'end')
#
# def worker_no_with(lock):
#     lock.acquire()
#     try:
#         print(threading.current_thread().getName(), 'start')
#         time.sleep(
