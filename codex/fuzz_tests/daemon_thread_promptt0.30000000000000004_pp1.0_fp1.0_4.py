import threading
# Test threading daemon
# import time
# import threading
#
#
# def worker():
#     print('Worker')
#     return
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

# Test threading daemon
# import time
# import threading
#
#
# def worker():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(2)
#     print(threading.currentThread().getName(), 'Exiting')
#
#
# def my_service():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(3)
#     print(threading.currentThread().getName(), 'Exiting')
#
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker',
