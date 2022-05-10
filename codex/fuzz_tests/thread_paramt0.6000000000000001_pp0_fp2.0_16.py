import sys, threading
threading.Thread(target=lambda: sys.stdout.write("foo!")).start()
</code>
... it will not print the message. So, how to get around this?

UPDATE: I've just tried this on a different machine, and it's working fine. So, it's not a Python issue, it's something wrong with my machine. I'm not sure what it could be, though... I've installed Anaconda Python, but I don't think that would have any effect on stdout.

