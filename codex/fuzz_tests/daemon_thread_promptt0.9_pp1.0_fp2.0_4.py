import threading
# Test threading daemon process
# def worker():
#     print threading.currentThread().getName(), 'Starting'
#     time.sleep(2) # sleep 5 sec
#     print threading.currentThread().getName(), 'Exiting'
#
# def my_service():
#     print threading.currentThread().getName(), 'Starting'
#     time.sleep(3) # sleep 5 sec
#     print threading.currentThread().getName(), 'Exiting'
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name
#
# w.start()
# w2.start()
# t.start()

# Test Synchronization primitives
# Lock

# class Counter(object):
#     def __init__(self):
#         self.count = 0
#
#     def increment(self, offset):
#         self.count += offset
#
# 
