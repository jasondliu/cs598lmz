import threading
threading.Thread(target=f).start()
</code>
This works just fine.
The problem is, I want to make <code>f</code> return the result of the process when it's done.
However, the following doesn't work:
<code>import threading
t = threading.Thread(target=f)
t.start()
t.join()
print "Done"
</code>
Here, the program just freezes at the <code>t.join()</code> line.
I also tried this:
<code>import threading
t = threading.Thread(target=f)
t.start()
res = f()
t.join()
print "Done"
</code>
but <code>res</code> remains <code>None</code>
Is there a way to make <code>f</code> return the result of <code>subprocess.Popen</code>?


A:

You can do this by subclassing <code>Thread</code>:
<code>class MyThread(threading.Thread):
    def __init__(self, *args,
