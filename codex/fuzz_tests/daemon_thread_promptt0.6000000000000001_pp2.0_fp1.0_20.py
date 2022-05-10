import threading
# Test threading daemon
import time
import os
import signal

def test_daemon():
    while True:
        print "I'm a daemon"
        time.sleep(1)

def test():
    while True:
        print "I'm a normal thread"
        time.sleep(1)

def signal_handler(signum, frame):
    print "Receive signal to exit"
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    t1 = threading.Thread(target=test_daemon)
    t2 = threading.Thread(target=test)
    t1.setDaemon(True)
    t1.start()
    t2.start()

    while True:
        time.sleep(1)
