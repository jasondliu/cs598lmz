import threading
# Test threading daemonmode
def worker():
    print("Main threa: {}".format(threading.currentThread().getName()))
    # All threads spawned from it will be daemon as well.
    print("Worker thread : {}".format(threading.currentThread().getName()))
    return

t = threading.Thread(name='Non-daemon thread', target=worker)
d = threading.Thread(name='Daemon thread', target=worker)
d.setDaemon(True)
# start the threads
d.start()
t.start()
d.join()
t.join()
