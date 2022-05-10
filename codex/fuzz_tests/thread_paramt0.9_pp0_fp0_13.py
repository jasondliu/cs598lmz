import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Coucou\n")).start()
</code>
Or you could use the <code>threading</code> module explicitly:
<code>import threading
t = threading.Thread(target=lambda: sys.stdout.write("Coucou\n"))
t.start()
# ...
t.join() # Wait for `t` to finish
</code>
Or yet another way:
<code>t = threading.Thread(target=sys.stdout.write, args=("Coucou\n",))
t.start()
t.join()
</code>

