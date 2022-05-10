import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start()
```

```Python
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys, threading
>>> threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start()
>>> Hello
```


## Part 1: Implement a thread-safe queue

The idea is to try and implement a thread-safe queue. This is a FIFO queue. This means that the elements enter from the tail of the queue and are removed from the head of the queue.

Here is an example of a normal queue:

```Python
# normal queue
q = Queue()
q.put(2)
q.put(3)
q.put(5)
q.get() # 2
q.
