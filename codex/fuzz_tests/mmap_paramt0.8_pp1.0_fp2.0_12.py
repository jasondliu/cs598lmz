import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
</code>
I get an empty string at the <code>print(m)</code> line.
I am trying to get the contents of a file (which is mostly going to be binary as I don't want to read line by line), so that I can pass it to a function which does some work on it.
Am I doing something wrong? Or is there a better way to do what I want to do?


A:

I think you are confused about the difference between bytes and byte strings.
<code>bytes</code> is a Python 3 type that represents an array of bytes,  They are intended for representing raw bytes and are not very useful for manipulating strings since they don't support text encoding/decoding.  If you need to manipulate strings, you should use the <code>str</code> type instead, which supports text encoding/decoding.
The <code>bytes</code> constructor takes only one parameter, <code>string</code>.  The <code>string</code> parameter must be a single <code>str</code> object, or a single <code>bytes</code> object (or subclass thereof).
