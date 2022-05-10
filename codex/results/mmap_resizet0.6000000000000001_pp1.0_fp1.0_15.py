import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>mmap.error: [Errno 22] Invalid argument</code>


A:

What you are trying to do is not supported by the mmap module. You can't mmap a file and then truncate it. 
The documentation says:
<blockquote>
<p>If the size of the file changes after you have created the mmap object, then the mmap object will reflect the new size. However, if the file decreases in size, the extra data in the mmap object is undefined. If the file increases in size, the extra data in the mmap object is filled with zeros.</p>
</blockquote>

