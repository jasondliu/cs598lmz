import threading
# Test threading daemon
import time

def daemon():
    print("Start daemon threading")
    time.sleep(10)
    print("Daemon done")

def non_daemon():
    print("Start non-daemon threading")
    time.sleep(2)
    print("Non-daemon done")

d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

t = threading.Thread(name="non-daemon", target=non_daemon)

d.start()
t.start()

d.join()
t.join()
