import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world\n")).start()
</code>
I wrote this code and I want to know why we use threading.Thread and start() in this code? 


A:

<code>threading.Thread</code> is a class, as in <code>threading.Thread(target=...)</code> you are calling its constructor.
As for <code>start()</code>, you are calling the thread's start method, which will make the thread run in parallel, so that you can use the <code>start()</code> method of other threads, making them run in parallel as well. 

