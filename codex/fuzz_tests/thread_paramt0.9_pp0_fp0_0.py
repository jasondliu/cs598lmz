import sys, threading
threading.Thread(target=lambda:sys.modules[__name__].__file__).start()
I get:
<code>Unhandled exception in thread started by &lt;function &lt;lambda&gt; at 0x1037b40c8&gt;
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;lambda&gt;
ValueError: couldn't create thread
</code>
Update: I noted that my virtualenvironment had a memory constraint:
<code>ulimit -a
-&gt; max memory size       (kbytes, -m) unlimited
-&gt; max locked memory     (kbytes, -l) 32
</code>
If I do <code>ulimit -l unlimited</code> the error doesn't occur. 
Why is this a problem? 


A:

I think there's two issues here; the first is that by running a function that calls <code>sys.modules[__name__].__file__</code> then the file containing the thread will stay in memory, as it is referenced as a global. A thread that waits 5 seconds
