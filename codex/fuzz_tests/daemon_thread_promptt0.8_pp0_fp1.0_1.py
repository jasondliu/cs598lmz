import threading
# Test threading daemon
def fun():
    print(threading.get_ident())
    while True:
        time.sleep(1)

threading.Thread(target=fun).start()

for t in threading.enumerate():
    print(t)
</code>
And if I run this using the command <code>python3 test.py</code>, I get the following output:
<code>140735750054208
&lt;_MainThread(MainThread, started 140735750054208)&gt;
&lt;Thread(Thread-1, started daemon 140735579542016)&gt;
&lt;_DummyThread(Dummy-1, started daemon 140735759643520)&gt;
</code>
So the <code>fun</code> function thread's status is <code>daemon</code>.
Now if I do the same thing in a Jupyter notebook:
<code>import time
import threading
# Test threading daemon
def fun():
    print(threading.get_ident())
    while True:
        time.sleep
