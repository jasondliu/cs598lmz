import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)))))
</code>
I get the following error:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Python27\lib\threading.py", line 810, in __bootstrap_inner
    self.run()
  File "C:\Python27\lib\threading.py", line 763, in run
    self.__target(*self.__args, **self.__kwargs)
  File "&lt;string&gt;", line 1, in &lt;lambda&gt;
IOError: [Errno 9] Bad file descriptor
</code>
I'm using Python 2.7.3. I've tried this on Windows 7 and Windows XP.
I've tried this on Python 3.2.2 and it works fine.
I've tried this on Python 2.6.6 and it works fine.
I've tried this on Python 2.7.2 and it works fine.
I've tried this on Python 2.7.3 with <code
