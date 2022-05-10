import sys, threading
threading.Thread(target=lambda: sys.stderr.write("you're in for some fun.")).start()
print "hi",
</code>
This will print <code>hi</code> even though before printing that it already stopped.

