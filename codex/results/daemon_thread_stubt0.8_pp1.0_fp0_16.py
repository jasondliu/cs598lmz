import sys, threading

def run():
    x = None
    while True:
        x = x or 3
        x = x + 1
        if (x % 1000) == 0:
            # Force a stack overflow.
            run()

for i in range(1000):
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

run()
</code>
It also reproduces a stack overflow but seems to do so in a way that is not infinite.  Sometimes I get about 50 stack overflows and then it successfully completes.  Sometimes I get about 100.  Sometimes I get one.  I don't seem to be able to reproduce a stack overflow that is so deep that the interpreter quits.  What could be causing this?

