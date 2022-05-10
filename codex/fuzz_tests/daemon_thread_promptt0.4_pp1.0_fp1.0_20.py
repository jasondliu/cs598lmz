import threading
# Test threading daemon

def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

def non_daemon():
    print('Starting:')
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# d.join()
t.join()

# import threading
#
# def worker():
#     """thread worker function"""
#     print('Worker')
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
#
# print(threads)

# import threading
# import time
#
# def worker():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(2)
#
