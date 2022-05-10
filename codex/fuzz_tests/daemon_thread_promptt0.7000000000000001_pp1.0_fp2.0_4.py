import threading
# Test threading daemon mode
import time 

def func():
    while True:
        print "hello"
        time.sleep(1)

t = threading.Thread(target=func)
t.setDaemon(True)
t.start()
print "main thread"

# Test threading and wait for thread's end
'''
import threading
import time

def func():
    print "hello"
    time.sleep(4)

t = threading.Thread(target=func)
t.start()
t.join()
print "main thread"
'''
