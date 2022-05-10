import threading
# Test threading daemon
# if __name__ == '__main__':
#     import time
#     def daemon():
#         print 'Starting:', time.time()
#         time.sleep(0.2)
#         print 'Exiting :', time.time()
#     d = threading.Thread(name='daemon', target=daemon)
#     d.setDaemon(True)
#     def non_daemon():
#         print 'Starting:', time.time()
#         print 'Exiting :', time.time()
#     t = threading.Thread(name='non-daemon', target=non_daemon)
#     d.start()
#     t.start()
#     d.join()
#     t.join()

# Test threading
# if __name__ == '__main__':
#     import time
#     def countdown(n):
#         while n > 0:
#             print 'T-minus', n
#             n -= 1
#             time.sleep(5)
#     t = threading.Thread(target=countdown, args
