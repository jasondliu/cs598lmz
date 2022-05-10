import sys, threading

def run():
    print "Hi! I'm a thread."
threads = []
for i in range(5):
    thread = threading.Thread(target=run)
    threads.append(thread)
    thread.start()
</code>

Output:
<code>Hi! I'm a thread.
Hi! I'm a thread.
Hi! I'm a thread.
Hi! I'm a thread.
Hi! I'm a thread.
</code>
If I kill the python process, I get the following results:
<code>Traceback (most recent call last):
  File "/Users/michaelherman/projects/python-projects/threads.py", line 13, in &lt;module&gt;
    thread.start()
  File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/threading.py", line 852, in start
    _start_new_thread(self._bootstrap, ())
RuntimeError: can't start new thread
</code>

I think that this is
