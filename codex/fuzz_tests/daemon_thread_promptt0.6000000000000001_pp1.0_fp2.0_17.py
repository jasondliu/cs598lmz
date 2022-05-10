import threading
# Test threading daemon
# def daemon():
#     print('Starting:')
#     time.sleep(2)
#     print('Exiting:')
#
# def non_daemon():
#     print('Starting:')
#     print('Exiting:')
#
# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)
#
# t = threading.Thread(name='non-daemon', target=non_daemon)
#
# d.start()
# t.start()

# Test threading lock
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args
