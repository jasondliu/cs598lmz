import threading
# Test threading daemon
import time
import random

def daemon():
    print("Starting:", threading.current_thread().name)
    time.sleep(random.randint(1, 5))
    print("Exiting:", threading.current_thread().name)

def non_daemon():
    print("Starting:", threading.current_thread().name)
    print("Exiting:", threading.current_thread().name)

if __name__ == "__main__":
    d = threading.Thread(name="daemon", target=daemon)
    d.setDaemon(True)

    t = threading.Thread(name="non-daemon", target=non_daemon)

    d.start()
    t.start()

    d.join()
    t.join()
