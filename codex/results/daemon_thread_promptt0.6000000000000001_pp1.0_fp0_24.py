import threading
# Test threading daemon
def test_daemon(name):
    print("Thread name: %s" % name)
    print("Thread name: %s" % threading.current_thread().name)
    print("Thread isAlive: %s" % threading.current_thread().is_alive())
    print("Thread daemon: %s" % threading.current_thread().daemon)
    print("Thread isDaemon: %s" % threading.current_thread().isDaemon())
    print("Thread activeCount: %d" % threading.active_count())
    print("Thread enumerate: %s" % threading.enumerate())
    time.sleep(1)
    print("Thread name: %s" % name)
    print("Thread name: %s" % threading.current_thread().name)
    print("Thread isAlive: %s" % threading.current_thread().is_alive())
    print("Thread daemon: %s" % threading.current_thread().daemon)
    print("Thread isDaemon: %s" % threading.current_thread
