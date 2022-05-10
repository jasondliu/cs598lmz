import threading
# Test threading daemon

def daemon():
    print("\nStarting:", threading.current_thread().name)
    time.sleep(2)
    print("\nExiting:", threading.current_thread().name)

def non_daemon():
    print("\nStarting:", threading.current_thread().name)
    print("\nExiting:", threading.current_thread().name)

d = threading.Thread(name="daemon", target=daemon, daemon=True)
t = threading.Thread(name="non-daemon", target=non_daemon)

d.start()
time.sleep(1)
t.start()
d.join()
t.join()
