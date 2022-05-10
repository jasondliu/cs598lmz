import threading
# Test threading daemon
def func_daemon():
    print("Running in a daemon thread")

if __name__ == "__main__":
    # Create a new thread as a daemon
    thread = threading.Thread(target=func_daemon)
    thread.setDaemon(True)
    thread.start()

    # Check if the main thread is a daemon
    print("Main thread is a daemon: {}".format(threading.current_thread().isDaemon()))
    threading.current_thread().setDaemon(False)
    print("Main thread is a daemon: {}".format(threading.current_thread().isDaemon()))
