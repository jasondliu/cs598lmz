import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b\x5b\x33\x3b\x4a')).start()
</code>
or
<code>echo -e "\x1b[3;J"
</code>
However, none of these work.


A:

I'm not sure, but my best guess is that you can't clear the scrollback buffer without changing the history size. The problem is that the scrollback buffer is not a simple list, but a circular buffer, with an index that points to the "line before the top".
See this blog post for an explanation how circular buffers work:
http://cglab.ca/~abeinges/blah/too-many-lists/book/intermezzo-3.html
There's also a Python module for that:
https://pypi.python.org/pypi/cycler
Anyway, the point is that there's no direct way to clear the scrollback buffer. You can only change the size of the buffer so that the index points to a different line.
You can try to change the scrollback buffer size to zero. I'm not sure if
