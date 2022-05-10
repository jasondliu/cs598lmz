import threading
# Test threading daemon
# def my_service():
#     print('Starting service')
#     time.sleep(1)
#     print('Exiting service')

# t = threading.Thread(name='my_service', target=my_service)
# t.start()
# t.join()
# print('Exiting main thread')

# Test threading non-daemon
# def my_service():
#     print('Starting service')
#     time.sleep(1)
#     print('Exiting service')

# t = threading.Thread(name='my_service', target=my_service)
# t.setDaemon(True)
# t.start()
# t.join()
# print('Exiting main thread')

# Test threading with lock
# def worker_with(lock):
#     with lock:
#         print('Lock acquired via with')

# def worker_no_with(lock):
#     lock.acquire()
#     try:
#         print('Lock acquired directly')
#     finally:
#         lock.release()

# lock =
