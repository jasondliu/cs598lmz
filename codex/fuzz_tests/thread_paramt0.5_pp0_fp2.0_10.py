import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10000000)))))
</code>
This is the error message:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Users\Pepsi\AppData\Local\Programs\Python\Python37-32\lib\threading.py", line 917, in _bootstrap_inner
    self.run()
  File "C:\Users\Pepsi\AppData\Local\Programs\Python\Python37-32\lib\threading.py", line 865, in run
    self._target(*self._args, **self._kwargs)
  File "&lt;ipython-input-2-1e00d6c68f1e&gt;", line 1, in &lt;lambda&gt;
    threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10000000)))))
  File "&lt;ipython-input-1-859bbd9c0b0f&
