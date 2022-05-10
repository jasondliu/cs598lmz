import threading
# Test threading daemon

def thread_function():
    a= time.sleep(1)
    print("thread function")

i=0
while True:
    i+=1
    x = threading.Thread(target=thread_function)
    x.setDaemon(True)
    x.start()
    x.join()
    print("Loop %s"%i)
    if i==1000:
        break
    
    
    
    

import threading
import time

# Test threading daemon

def thread_function():
    a= time.sleep(1)
    print("thread function")

i=0
while True:
    i+=1
    x = threading.Thread(target=thread_function)
    x.setDaemon(True)
    x.start()
    x.join()
    print("Loop %s"%i)
    if i==1000:
        break

# Test multithreading

import threading
import time

def thread_function(a,b,c):
    a= time.sleep(1)
    print
