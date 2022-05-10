import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
threading.Thread(target=lambda: sys.stdout.write("world\n")).start()
</code>
But when I run the code, I get the following output:
<code>$ python3 test.py
world
hello
</code>
Can someone explain why this happens? I would expect the order of output to be the same as the order in which the two threads are started.


A:

The output ordering is arbitrary and has to do with the way the threads are scheduled by the operating system and the Python VM.

