import threading
# Test threading daemon

#import time

#def sleeper(i):
#    print ("thread %d sleeps for 5 seconds" % i)
#    time.sleep(5)
#    print ("thread %d woke up" % i)

#for i in range(10):
#    t = threading.Thread(target=sleeper, args=(i,))
#    t.start()

import time
import threading

def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
