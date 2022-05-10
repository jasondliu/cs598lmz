import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
I do not understand why the output is <code>b'\x01'</code>. I thought it should be <code>b'\x00'</code> since I wrote <code>0</code> to the file.


A:

The problem is that you are writing a <code>bytes</code> object, but you are reading an <code>int</code>.
The <code>bytes</code> object <code>bytes(1)</code> is equivalent to <code>b'\x01'</code> (one byte with value 1).
When you write <code>m[0] = 0</code>, you are writing the integer 0 to the memory-mapped file, which is equivalent to the byte <code>b'\x00'</code>.
When you read the file with <code>f.read()</code>, you are reading it as an <code>int</code>.
If you read the file as a <
