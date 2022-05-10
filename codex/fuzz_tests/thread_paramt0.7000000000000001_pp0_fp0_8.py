import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world")).start()
</code>
will print <code>hello world</code> to stdout, but
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world\n")).start()
</code>
will not.  Not all of the characters in the string will be written to stdout.
The only thing I can think of is that there is some kind of race condition, but I cannot figure out what is going on.
I am running Windows 7 x64 with Python 2.7.
EDIT: I think I have figured out what is going on.  When I changed the code to read
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world\n")).start()
sys.stdout.flush()
</code>
it worked.  It appears that the output buffer is not flushed until after the program terminates.  Is there any way to flush the output buffer without terminating the program?


A:

You could try using <code>sys.stdout.
