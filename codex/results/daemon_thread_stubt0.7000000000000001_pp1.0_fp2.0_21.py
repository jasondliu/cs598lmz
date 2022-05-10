import sys, threading

def run():
    sys.stdout.write("1")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()
</code>
The above code will print "1" in the Python console.
I've tried doing the following:
<code>import sys, threading

def run():
    sys.stdout.write("1")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

print repr(thread.stdout)
</code>
But it returns <code>&lt;closed file '&lt;stdout&gt;', mode 'w' at 0x0000000002B32EA0&gt;</code>.
My question is, how can I get the stdout of a thread while it is running?


A:

That's not how it works. <code>sys.stdout</code> is a global variable that's shared by all threads. It doesn't have a per-thread value.
The only way to read what a thread has written to <code>sys.stdout</code
