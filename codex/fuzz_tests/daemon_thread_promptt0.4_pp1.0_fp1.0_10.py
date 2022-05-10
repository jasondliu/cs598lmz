import threading
# Test threading daemon
# import time
# import threading
#
# def worker():
#     print(threading.current_thread().getName(), 'Starting')
#     time.sleep(0.2)
#     print(threading.current_thread().getName(), 'Exiting')
#
# def my_service():
#     print(threading.current_thread().getName(), 'Starting')
#     time.sleep(0.3)
#     print(threading.current_thread().getName(), 'Exiting')
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name
#
# w.start()
# w2.start()
# t.start()

# Test threading lock
# import threading
# import time
#
# class Box(object):
#     lock = threading.RLock()
#
#     def __init__(self):
#         self.total_items
