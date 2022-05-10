import threading
# Test threading daemon
def testThread():
    for i in range(10):
        print "This is a test thread :%d" % i
        time.sleep(1)
thread = threading.Thread(target=testThread, args=())

# 修改线程的超时时间，
import socket
import threading
import time

def set_timeout(num, callback):
    socket.setdefaulttimeout(num)
    try:
        result = callback()
    except socket.timeout:
        print "Timeout"
    finally:
        socket.setdefaulttimeout(None)
    return result

def test_timeout():
    for i in range(10):
        print i
        time.sleep(1)

def test():
    threading.Timer(10, set_timeout(20, test_timeout)).start()

test()

# 核心是用threading.Timer创建一个定时器，用socket.setdefaulttimeout设置
