import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
This code prints <code>b'\x00'</code>, but I expected it to print <code>b'\x01'</code>.
I'm using Python 3.5.2.


A:

The first <code>f.write</code> call flushes the file buffer, and the file is closed and reopened when you open it again in the <code>with</code> block.
You can force a flush by calling <code>f.flush()</code> after the first <code>f.write</code> call.

