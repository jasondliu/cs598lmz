import threading
threading.BoundedSemaphore
</code>
and the error is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'BoundedSemaphore'
</code>


A:

In Python 3.5, <code>threading.BoundedSemaphore</code> is a subclass of <code>threading._BoundedSemaphore</code>.  Your actual error is:
<code>&gt;&gt;&gt; threading._BoundedSemaphore
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute '_BoundedSemaphore'
</code>
Over in the Python source, <code>threading.py</code> defines <code>BoundedSemaphore</code> as a subclass of <code>_BoundedSemaphore</code>, as you described.  But it
