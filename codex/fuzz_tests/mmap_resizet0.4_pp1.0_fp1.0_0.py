import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: mmap closed or invalid</code> at the last line.
I know that the <code>mmap</code> object is invalidated when the file is truncated. But I don't know if it is possible to get the bytes from the <code>mmap</code> object before truncating the file.
I want to get the bytes from the <code>mmap</code> object, truncate the file, and then write the bytes to the file.
I am using Python 3.7.3 on Windows 10.


A:

The problem is that you are trying to read from the <code>mmap</code> object after you have truncated the file.  You need to read the bytes before you truncate the file.  I don't know why you are truncating the file in the first place.  The following code works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fil
