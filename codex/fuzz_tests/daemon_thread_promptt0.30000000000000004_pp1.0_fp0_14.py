import threading
# Test threading daemon
# def worker():
#     print("worker")
#     time.sleep(1)
#     print("worker")
#
# t = threading.Thread(target=worker)
# t.daemon = True
# t.start()
# print("main thread")

# Test threading lock
# lock = threading.Lock()
# def worker():
#     lock.acquire()
#     print("worker")
#     time.sleep(1)
#     print("worker")
#     lock.release()
#
# t = threading.Thread(target=worker)
# t.start()
# print("main thread")

# Test threading condition
# condition = threading.Condition()
# def worker():
#     condition.acquire()
#     condition.wait()
#     print("worker")
#     time.sleep(1)
#     print("worker")
#     condition.release()
#
# t = threading.Thread(target=worker)
# t.start()
# time.sleep(1)
# condition.acquire()
# condition
