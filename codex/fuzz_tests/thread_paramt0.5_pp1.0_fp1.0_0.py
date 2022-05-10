import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
</code>
This will print <code>hello</code> in the terminal.

