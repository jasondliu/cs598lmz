import threading
# Test threading daemon
class TestDaemon(threading.Thread):
    def run(self):
        for item in range(1,100):
            print(item)
t1 = TestDaemon()
t1.daemon = True
t1.start()
for item in range(101,200):
    print(item)
'''
import threading
# Test threading join
class TestJoin(threading.Thread):
    def run(self):
        print("thread start")
        for item in range(1,10):
            print(item)
        print("thread end")
t1 = TestJoin()
t1.start()
t1.join()
print("main end")
'''
'''
import threading
import time
# Test threading
class TestDaemon(threading.Thread):
    def run(self):
        for item in range(1,100):
            print(item)
        time.sleep(1)
for item in range(1,10):
    t1 = TestDaemon()
    t1.setDaemon(True)
    t1.start
