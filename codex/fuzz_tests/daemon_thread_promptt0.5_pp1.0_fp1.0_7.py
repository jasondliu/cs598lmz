import threading
# Test threading daemon
# Threading
#     daemon:
#         Daemon threads are service threads that typically run without blocking to service other threads.
#         The entire Python program exits when no alive non-daemon threads are left.
def worker(num):
    print("Worker: %s" % num)
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    # t.setDaemon(True)
    threads.append(t)
    t.start()
# print(threading.activeCount())
# print(threading.enumerate())
# print(threading.currentThread())

for t in threads:
    t.join()
