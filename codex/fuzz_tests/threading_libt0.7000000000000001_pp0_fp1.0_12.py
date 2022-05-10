import threading
threading.Thread(target=lambda: time.sleep(100)).start()
</code>
It results in a <code>RuntimeError: can't start new thread</code> :
<code>---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
&lt;ipython-input-1-bd03d7f7b8f8&gt; in &lt;module&gt;
      1 import threading
----&gt; 2 threading.Thread(target=lambda: time.sleep(100)).start()

/Users/jean-christophe/.local/share/virtualenvs/test-1zQdGgZ7/lib/python3.7/threading.py in start(self)
   1330 
   1331         assert self._initialized, "Thread.__init__() not called"
-&gt; 1332         _start_new_thread(self._bootstrap, ())
   1333 
   1334     def run(self):

RuntimeError: can't start new thread
</code>
I'm using python 3.7.6 in a virtualenv (
