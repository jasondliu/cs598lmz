import threading
# Test threading daemon
# def worker():
#     print 'Worker'
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     t.start()
#     threads.append(t)
#
# print threads

# t = threading.Thread(target=worker)
# t.start()

# Test threading lock
# lock = threading.Lock()
#
# def worker():
#     for i in range(5):
#         lock.acquire()
#         print 'Worker'
#         lock.release()
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

# Test threading RLock

# lock = threading.RLock()
#
# def worker():
#     for i in range(5):
#         lock.acquire()
#         print '
