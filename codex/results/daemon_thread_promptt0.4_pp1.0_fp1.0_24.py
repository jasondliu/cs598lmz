import threading
# Test threading daemon
# import time
# import threading
#
#
# def worker():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(5)
#     print(threading.currentThread().getName(), 'Exiting')
#
#
# def my_service():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(10)
#     print(threading.currentThread().getName(), 'Exiting')
#
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker)  # use default name
#
# w.start()
# w2.start()
# t.start()

# Test threading lock
# import threading
# import time
#
#
# class Box(object):
#     lock = threading.RLock()
#
#     def __init__(self):
#         self.total_
