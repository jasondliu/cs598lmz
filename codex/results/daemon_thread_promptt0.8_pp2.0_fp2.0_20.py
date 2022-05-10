import threading
# Test threading daemon with exit code.
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)
d  = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)
def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)
t = threading.Thread(name="non-daemon", target=non_daemon)
d.start()
t.start()
d.join()
t.join()
# Start a thread with a different name
w = threading.Thread(target=daemon, name="daemon2")
w.start()
w.join()
