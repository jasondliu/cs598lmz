import sys, threading

def run():
    while True:
        sys.stdout.write("Hello")
        sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

while True:
    sys.stdout.write("World")
    sys.stdout.flush()
</code>
This is the output I get (sometimes):
<code>HelloWorldHelloWorld
</code>
However, what I actually want is something like:
<code>HelloWorldHello
World
</code>
So the second thread flushes the output buffer.
How do I do this?
I tried to replace <code>sys.stdout.flush()</code> with <code>sys.stdout.flush(1)</code> and <code>sys.stdout.flush(2)</code> and even <code>sys.stdout.flush("t")</code>, but it just doesn't work.
Thanks!


A:

<code>stdout</code> is a file object; it has no method <code>flush(2)</code> and the <code>flush()</code> method doesn't
