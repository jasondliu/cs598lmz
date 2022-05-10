import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I was expecting that <code>a</code> would be a zero-length byte string, but instead I got:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I'm guessing that the reason is that <code>mmap</code>'s fd reference to the file is invalidated by the <code>truncate</code> call, even though the <code>m</code> object still points to the same memory address.
Is there a way to truncate a file while still keeping the <code>mmap</code>'d section valid?


A:

I've found a way to do this by using <code>mmap.resize</code>:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
    print(a)
</code>
This prints
