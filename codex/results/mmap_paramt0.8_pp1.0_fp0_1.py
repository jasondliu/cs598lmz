import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())
    m.seek(0)
    m.write_byte(bytes(1))
</code>
which causes
<code>TypeError: a bytes-like object is required, not 'int'
</code>
I get the same error if I use <code>bytearray</code>.
How do I write the value <code>1</code> to the file?


A:

The <code>bytes</code> and <code>bytearray</code> types support an imperative <code>__setitem__</code>/<code>__getitem__</code> interface, but not an imperative <code>__add__</code> interface, which means any operation expecting a <code>bytes</code>-like object to be passed to it must use the <code>__getitem__</code> interface.
So, the proper way to write a <code>bytes</code> value to a file is:
<code>with open('test', 'wb') as f:
    f.write(bytes([1]))
</code>
and
