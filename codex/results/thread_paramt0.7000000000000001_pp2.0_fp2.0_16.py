import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abc'), daemon=True).start()
</code>
However, the output is not <code>abc</code>.
The code above is from this question. I have tested it with Python 3.7.7 and it is running on Ubuntu 19.10.


A:

There are two issues here:

The default <code>io.TextIOWrapper</code> encoding for <code>sys.stdout</code> is <code>UTF-8</code>. So if you try to write a <code>str</code> that contains non-ASCII characters, you get a <code>UnicodeEncodeError</code>. This can be solved by changing the encoding to <code>sys.stdout.reconfigure(encoding='ascii')</code>.
Since you're using the <code>Thread</code> class and not the <code>concurrent.futures.ThreadPoolExecutor</code> class, you need to join the thread before exiting the main thread, otherwise the application will exit before the thread finishes writing to <code>sys.stdout</code>. This can be solved
