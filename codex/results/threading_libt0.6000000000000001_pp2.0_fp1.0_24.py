import threading
threading.Thread(target=func1).start()
threading.Thread(target=func2).start()
</code>
When I run this code, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    threading.Thread(target=func1).start()
  File "/usr/lib/python2.7/threading.py", line 745, in start
    _start_new_thread(self.__bootstrap, ())
thread.error: can't start new thread
</code>
I am trying to understand why I am getting this error. Any help is much appreciated.

