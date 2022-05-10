import threading
# Test threading daemon thread
def daemon():
    print("Starting daemon...")
    time.sleep(2)
    print("Exiting daemon...")
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print("Starting non-daemon...")
    print("Exiting non-daemon...")
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join()
t.join()
