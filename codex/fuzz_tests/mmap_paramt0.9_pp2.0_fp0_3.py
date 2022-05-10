import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'3')

    s = struct.Struct('&lt;h')
    fmt = '{0:x}'.format(s.unpack(m[0:2])[0])  # unpack is successful here, but memory content at &lt;h is not updated
</code>
If I print the value of m[0:2], I can see that it remains '01' and not changed to '03'.
I don't want to 'flush' the map everytime I update. Is there a way to read the updated values or update the memory?
I'm using Python 3.5.2 on Ubuntu 16.04
I have also tried this : mmap.mmap reads wrong values but it doesn't work unless I <code>m.flush()</code>


A:

If you are using Python3, consider using memoryview which provides almost the same functionality but better interface.
Here is your code:
<code>import struct

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as
