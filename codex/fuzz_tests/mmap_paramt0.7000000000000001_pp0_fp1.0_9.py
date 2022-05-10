import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()
</code>
A byte is still not a byte. A byte is an integer between 0 and 255. To write the byte <code>2</code> to the file, you need to write the byte <code>2</code>, not <code>'2'</code>. Note that in Python 2, <code>bytes('2')</code> is not the same as <code>b'2'</code>. The former is the string <code>'2'</code> encoded with the default encoding (which is ASCII on most systems) while the latter is the single-element <code>bytes</code> object containing the single byte <code>2</code>.
In Python 3, <code>bytes</code> is a builtin, and <code>bytes(1)</code> creates a single-element <code>bytes</code> object containing the single byte <code>1</code>. In Python 2, you need to use <code>bytearray</code> to create a single-element <code>bytes</code> object.
The <code>os</
