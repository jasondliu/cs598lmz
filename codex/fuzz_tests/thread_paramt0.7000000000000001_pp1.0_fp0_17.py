import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world\n")).start()

# Python 2.x
import thread
thread.start_new_thread(lambda: sys.stdout.write("hello world\n"), ())
</code>

