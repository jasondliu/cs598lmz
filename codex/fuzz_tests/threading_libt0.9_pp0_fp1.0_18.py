import threading
threading.ThreadError

from multiprocessing import Process, Lock, Value
from os import getpid

from time import sleep

from threading import Event
</code>


A:

Try running it as <code>python -i example.py</code> and see if your interactive interpreter gives you any more output.
Edit for new information
When you run your program, it is finding all the constants at the top level of the <code>threading</code> module, and attaching them to the global namespace.
You can see them here: http://docs.python.org/library/threading.html
Try this (note the whitespace changes):
<code>import threading

def x():
    print threading.ThreadError

x()
</code>

