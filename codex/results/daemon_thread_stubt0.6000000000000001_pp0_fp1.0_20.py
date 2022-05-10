import sys, threading

def run():
    sys.setcheckinterval(100)
    print "running"
    while True:
        pass

t = threading.Thread(target=run)
t.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print "interrupted"
</code>
If you run this script, it will print "running" and then do nothing until you press Ctrl-C.
But if you change the line
<code>sys.setcheckinterval(100)
</code>
into
<code>sys.setcheckinterval(10)
</code>
then it will print "running" and then print "interrupted" immediately.
What is going on?


A:

As the documentation says, setting the check interval to a low value (e.g. 1 or 10) can cause your program to run slower. The reason for this is that the check interval determines how often the interpreter checks for signals. If you set it to 1, then the interpreter will check for signals on every bytecode instruction. If you set it to 10, it will check on every 10th bytecode instruction.
In the first
