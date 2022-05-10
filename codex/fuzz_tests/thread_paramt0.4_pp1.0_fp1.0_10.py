import sys, threading
threading.Thread(target=lambda: sys.stdout.write("test\n")).start()
</code>
This works fine on my system, but it's not portable because it relies on the OS's threading implementation.
Is there a portable way to do this?

