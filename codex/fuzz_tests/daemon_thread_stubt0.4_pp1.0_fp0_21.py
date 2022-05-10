import sys, threading

def run():
    while True:
        try:
            t = threading.Thread(target=run)
            t.start()
        except:
            pass

run()
</code>
This code is supposed to create a threading loop, but it doesn't. It just prints this:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Python34\lib\threading.py", line 921, in _bootstrap_inner
    self.run()
  File "C:\Python34\lib\threading.py", line 869, in run
    self._target(*self._args, **self._kwargs)
  File "C:/Users/alex/Desktop/threading.py", line 7, in run
    t = threading.Thread(target=run)
  File "C:\Python34\lib\threading.py", line 847, in __init__
    _start_new_thread(self._bootstrap, ())
RuntimeError: can't start new thread
</code>
Can anyone help me fix this?


A:
