import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48
    m.close()
</code>
I get the error: <code>TypeError: must be read-write buffer, not mmap</code>
I am using Python 3.4.3


A:

You are using the <code>bytes</code> constructor to create a <code>bytes</code> object.  That constructor takes an integer that specifies the length of the new <code>bytes</code> object.  You are passing <code>1</code>, so you are creating a <code>bytes</code> object with length 1.  The <code>bytes</code> object is immutable, so you cannot change it.
You can create a mutable <code>bytearray</code> object by using the <code>bytearray</code> constructor instead.  The <code>bytearray</code> constructor takes a single argument that specifies the initial value of the <code>bytearray</code> object.  You can pass a <code>bytes</code> object, a <code>str</code> object, or an iterable of integers. 
