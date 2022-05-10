import threading
# Test threading daemon
import time

def func():
    print "In func"
    time.sleep(5)
    print "End func"

if __name__ == '__main__':
    daemon = threading.Thread(target=func)
    daemon.daemon = True
    daemon.start()
    print "Started"
    time.sleep(1)
    print "End"
