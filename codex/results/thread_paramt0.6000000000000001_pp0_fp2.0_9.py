import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(str(i) for i in range(10)))).start()
</code>
I'd like to do the same thing in Python 3, but I can't get the syntax right.  It seems like it should be easy, but I can't figure out the right syntax.  The following is the best I could come up with, but it doesn't work:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(str(i) for i in range(10)))).start()
</code>
I get the following error:
<code>  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.1/threading.py", line 488, in start
    _start_new_thread(self.__bootstrap, ())
TypeError: 'str' object is not callable
</code>
Any ideas?


A:

You need to use the <code>print</code> function in Python 3:
