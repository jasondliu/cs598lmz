import sys, threading
threading.Thread(target=lambda: sys.stdout.write(threading.currentThread().name)).start()
</code>
Output:
<code>Thread-1
</code>
Update as per comment:
<blockquote>
<p>How can I do this on Python 2?</p>
</blockquote>
Well, you can make it work on Python 2.7.12 (I can't personally test on any other Python 2 version) like this:
<code>import threading
print threading.currentThread().getName()
</code>
Python 2 vs Python 3

