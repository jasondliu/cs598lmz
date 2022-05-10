import sys, threading
threading.Thread(target=lambda: sys.stdout.write('multiple threads.\n')).start()
</code>
Question: 
I don't understand why they are printing "multiple threads." <code>threading.Thread(target=lambda: sys.stdout.write('multiple threads.\n')).start()</code> will produce a thread for sure, but I don't see why that thread will actually print something. Also, since <code>start()</code> is not a blocking call, how does the program wait for it to complete before proceeding to the next instruction?
P.S. I don't know anything about multithreading/concurrency.


A:

The reason you're seeing <code>"multiple threads."</code> is because you're using <code>threading.Thread()</code> in its simplest form:

<code>TransientWorkerThread.__bootstrap(self)</code> on the <code>start()</code> will create a <code>_thread.start_new_thread()</code> which executes your <code>lambda</code>
Your code is a bare <code>lambda</code> which <code>.start
