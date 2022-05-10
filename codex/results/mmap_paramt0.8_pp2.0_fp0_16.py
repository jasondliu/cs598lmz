import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'\x00' * 100)
    m.seek(0)
    m.write(b'\x00' * 100)
</code>
When I wrote my question, I was experiencing the <code>WindowsError: [Error 22] Invalid argument</code> exception.  It then occurred to me to try using just the <code>with</code> statement instead of the <code>with</code> <code>as</code> syntax, and lo and behold, everything worked out.  (Albeit, I got the same exception after many successful runs.)
I tried to reproduce the error by running the code above repeatedly, but it works.  The answer is good, but it would be nice to know exactly why this error occurs.

