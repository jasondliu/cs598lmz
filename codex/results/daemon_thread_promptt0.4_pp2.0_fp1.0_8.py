import threading
# Test threading daemon

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
</code>
I get the following error:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 552, in __bootstrap_inner
    self.run()
  File "/usr/lib/python2.7/threading.py", line 505, in run
    self.__target(*self.__args, **self.__kwargs)
TypeError: 'NoneType' object is not callable
</code>
I am using Python 2.7.6 on Ubuntu 14.04.
What am I doing wrong?


A:

You need to return something from the function, even if it's <code>None</code>.
<code>def worker():
    """thread worker function"""
    print 'Work
