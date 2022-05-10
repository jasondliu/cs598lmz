import threading
threading.stack_size(67108864)

def func():
    print("thread")

t = threading.Thread(target=func)
t.start()
t.join()
</code>
I get this error:
<code>Fatal Python error: PyThreadState_Get: no current thread

Thread 0x00007fa1d3b8c740 (most recent call first):
  File "/usr/lib/python3.6/threading.py", line 884 in _bootstrap_inner
  File "/usr/lib/python3.6/threading.py", line 916 in _bootstrap

Aborted (core dumped)
</code>
What does this error mean?


A:

You need to call <code>threading.stack_size()</code> before you import anything else.
<code>threading.stack_size(67108864)
import threading

def func():
    print("thread")

t = threading.Thread(target=func)
t.start()
t.join()
</code>

