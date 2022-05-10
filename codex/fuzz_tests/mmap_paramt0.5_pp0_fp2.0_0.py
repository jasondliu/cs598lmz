import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())
    m.write_byte(bytes(2))
</code>
But I get the following error:
<code>TypeError: an integer is required (got type bytes)
</code>
I don't understand why <code>bytes(2)</code> is not an integer. What should I do to fix this?


A:

<code>bytes(2)</code> is a <code>bytes</code> object. You need to pass in an integer, so <code>2</code> is what you want.

