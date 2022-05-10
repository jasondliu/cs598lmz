import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'5'
    m.flush()
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
This code produces output <code>5</code> , but I would like to produce <code>51</code> .
I have tried to set offset in mmap call to 1 byt and open file in append mode, but it doesn't work in both cases.
How to do it?


A:

You can simply do this like this:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1] = b'5'
    m.flush()
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
However, this will only work if the file already has content at that offset. In order to do what you
