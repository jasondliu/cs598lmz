import sys, threading
threading.Thread(target=lambda: threading.local().foo).start()
</code>
Will produce this result:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 552, in __bootstrap_inner
    self.run()
  File "/usr/lib/python2.7/threading.py", line 505, in run
    self.__target(*self.__args, **self.__kwargs)
  File "&lt;string&gt;", line 1, in &lt;lambda&gt;
AttributeError: 'thread._local' object has no attribute 'foo'
</code>
According to the documentation for <code>_threading_local</code>, it says:
<blockquote>
<p>Return a new local object.</p>
<p>If <code>&lt;code&gt;args&lt;/code&gt;</code> is given, they are passed to the object’s <code>&lt;code&gt;__init__()&lt;/code&
