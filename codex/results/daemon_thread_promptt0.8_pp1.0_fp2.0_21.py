import threading
# Test threading daemon with logging messages
def log_thread():
    threading.current_thread().setName("Log")
    logging.debug("Thrlog: Hello!")
    time.sleep(3)
    logging.debug("Thrlog: Goodbye!")
    return
threading.Thread(target=log_thread).start()
# Test threading daemon with a simple thread
def thr():
    threading.current_thread().setName("Thr")
    for i in range(10):
        print("Thr: printing", i)
        time.sleep(.2)
    print("Thr: done")
threading.Thread(target=thr).start()
# Test threading daemon with a daemon thread
def thr_daemon():
    threading.current_thread().setName("ThrDaemon")
    for i in range(10):
        print("ThrDaemon: printing", i)
        time.sleep(.2)
    print("ThrDaemon: done")
thr_daemon = threading.Thread(target=thr_daemon)
thr_daemon
