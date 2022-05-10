import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The code above should print <code>b'\x00'</code>, but I got a <code>ValueError</code> says "mmap length is greater than file size".
The question is, why does <code>mmap.mmap</code> fail to truncate the file when <code>file.truncate</code> succeeds? And, how can I use <code>mmap</code> and <code>file.truncate</code> together?


A:

The problem here is that you are trying to read from a file, but the content of the file has been truncated, so there is no content to read.
<code>ValueError: mmap length is greater than file size
</code>
You are trying to read more bytes than the file has, so it cannot perform the operation.

