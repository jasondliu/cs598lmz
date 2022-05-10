import sys, threading
threading.Thread(target=lambda: sys.stdout.write("blah\n")).start()
</code>


A:

You can lock <code>stdout</code> and <code>stderr</code> as you print, and then unlock to prevent the other thread from printing over your output.
<code>import sys
import threading
import time

def f1():
    time.sleep(1)
    print("f1")
    sys.stdout.flush()

def f2():
    time.sleep(1)
    print("f2")
    sys.stdout.flush()

threading.Thread(target=f1).start()
threading.Thread(target=f2).start()

time.sleep(5)
</code>
prints the following two lines, while other unsafe examples will print this instead:
<code>f1
f2
</code>
<code>f2f1
</code>
which is probably not what you want.

