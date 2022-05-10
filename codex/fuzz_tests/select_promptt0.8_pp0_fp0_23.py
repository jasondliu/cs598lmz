import select
# Test select.select():
r = select.select([sys.stdin], [], [], 10)
if r[0]:
    print("Got input!")
else:
    print("No input!")

# Test select.poll():
p = select.poll()
p.register(sys.stdin)
r = p.poll(10)
if r[0][1] & select.POLLIN:
    print("Got input!")
else:
    print("No input!")
</code>
On Windows, both produce the same result: I get "No input!" as output after 10 seconds, no matter whether I press a key or not.
Why is that?


A:

I got it to work by opening the console in a nonblocking manner:
<code>import os
import msvcrt,sys

msvcrt.setmode(sys.stdin.fileno(), os.O_NONBLOCK)
</code>

