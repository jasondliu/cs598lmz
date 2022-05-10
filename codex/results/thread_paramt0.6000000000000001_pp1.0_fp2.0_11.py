import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from stdout\n")).start()
threading.Thread(target=lambda: sys.stderr.write("Hello from stderr\n")).start()
</code>
You will see that the order of the messages is unpredictable.

