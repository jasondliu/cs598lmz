import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read()), args=()).start()
</code>
My question is: Why is this failing?


A:

The reason that <code>sys.stdin.read()</code> blocks is because it is waiting for you to close the pipe.  If it does not receive an EOF it will forever sit there waiting for you to close the pipe.  You can close the pipe using <code>os.close(0)</code>, but that will also close the pipe on your prompt, so it will not work in this case.
What you can do instead is use <code>sys.stdin.read(1)</code> in a loop.  This will not block.  The <code>read()</code> function will also block if you try reading more bytes than it has available, so you need to use <code>read(1)</code> to read one byte at a time.  That's fine though, because you can use <code>sys.stdout.write(chunk)</code> to write one character at a time.
<code>import sys

def redirect_input():
