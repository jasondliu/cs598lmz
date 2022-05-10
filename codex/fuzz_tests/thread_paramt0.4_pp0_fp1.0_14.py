import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10000000)))))
</code>
This should print numbers from 1 to 10 million. But it does not.
Why?


A:

You must call <code>start()</code> on the thread to start it.
<code>&gt;&gt;&gt; t = threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10000000)))))
&gt;&gt;&gt; t.start()
</code>

