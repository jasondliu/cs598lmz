import sys, threading
threading.Thread(target=lambda: sys.stdin.read(), args=()).start()
 
import time
def foo():
    while True:
        print('foo')
        time.sleep(1)
 
t = threading.Thread(target=foo)
t.daemon = True
t.start()
 
while True:
    print('bar')
    time.sleep(2)
    if not threading.active_count():
        break
