import sys, threading

def run():
    i = 2
    while(True):
        print("Hello from thread %i" % i)
        time.sleep(1)
        i += 2

t = threading.Thread(target = run)
t.start()
```

```
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import threading, time
>>> def run():
...     i = 2
...     while(True):
...         print("Hello from thread %i" % i)
...         time.sleep(1)
...         i += 2
... 
>>> t = threading.Thread(target = run)
>>> t.start()
Hello from thread 2
Hello from thread 4
Hello from thread 6
Hello from thread 8
Hello from thread 10
Hello from thread 12
...
...
```

## 7 Multiprocessing
