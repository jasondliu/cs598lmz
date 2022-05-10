import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    m.write(bytes(2))
    m.flush()
    m.close()


with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    print(m.read()) # throws IOError
    m.close()
</code>
Throws an exception:
<code>IOError: [Errno 22] Invalid argument
</code>
Why does it happen? How can I overcome this?


A:

<blockquote>
<p>Why does it happen</p>
</blockquote>
Read more carefully. The exception thrown is <code>ValueError</code>, not <code>IOError</code>:
<code>ValueError: mmap length is zero
</code>
This is expected. You have opened your file and then mapped the whole file -- which is empty. You can either try to map the whole file or none of it or at least 1 byte of it:
<code>m = mmap.mmap(f.fileno(), 0)
...
m = mmap.mmap(f
