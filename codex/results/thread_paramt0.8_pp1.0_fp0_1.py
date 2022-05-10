import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
</code>
And that was pretty much it!

