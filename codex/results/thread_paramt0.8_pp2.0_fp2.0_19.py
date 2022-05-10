import sys, threading
threading.Thread(target=lambda: sys.stdout.write("abc\n")).start()
</code>
The result is:
<code>abc
</code>
Does Python not flush the output file periodically when there is output?


A:

The test code is working as expected. The output is flushed when you return to the main thread.
<code>threading.Thread(target=lambda: sys.stdout.write("abc\n")).start()
</code>
This starts a thread and returns to the main thread.
<code>sleep(10)
</code>
While the main thread is sleeping, the background thread writes to <code>stdout</code> and returns. <code>stdout</code> is not flushed until the main thread returns to the Python interpreter.
The easiest way to see this is to remove the <code>sleep</code> call. The output appears immediately:
<code>$ python3 file.py
abc
</code>
You can flush <code>stdout</code> by calling <code>flush</code> on it:
<code>threading.Thread(target=lambda: sys.stdout.
