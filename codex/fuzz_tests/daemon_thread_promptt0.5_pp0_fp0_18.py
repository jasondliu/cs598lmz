import threading
# Test threading daemon
# def worker():
#     print(threading.current_thread().name, 'Starting')
#     time.sleep(0.2)
#     print(threading.current_thread().name, 'Exiting')
#
# def my_service():
#     print(threading.current_thread().name, 'Starting')
#     time.sleep(0.3)
#     print(threading.current_thread().name, 'Exiting')
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name
#
# w.start()
# w2.start()
# t.start()

# ######################################################################################################################
# # Test threading lock
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     # 先存后取，结果应该为0
