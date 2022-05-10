import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>ValueError: mmap length is zero
</code>
I understand that mmap is not able to read from a file that has been truncated. However, I am wondering if there is a way to do this, or if I am approaching the problem the wrong way.
I am trying to implement a file that can be read from and written to at the same time. The file is appended to, and then read from. I want to be able to read from it while it is being written to.


A:

You need to call <code>mmap.resize()</code> to resize the memory map after you've truncated the file.

