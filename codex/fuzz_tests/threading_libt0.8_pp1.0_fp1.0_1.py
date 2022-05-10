import threading
threading.Thread(target=lambda: print("a"))
</code>
and 
<code>import threading
threading.Thread(target=print,args=("a",))
</code>
These two snippets seem to handle the same function differently. The first one will print out <code>a</code> instantly, while the second one does nothing. 
I wonder what's the difference between them.


A:

When you run the following code:
<code>import threading
threading.Thread(target=print,args=("a",))
</code>
It creates a thread, but it doesn't run the thread. You need to call the method <code>start</code> of this thread to run the thread:
<code>import threading
t=threading.Thread(target=print,args=("a",))
t.start()
</code>
This will print <code>"a"</code> only if you run the thread.
If you use this code:
<code>import threading
threading.Thread(target=lambda: print("a"))
</code>
It also creates a
