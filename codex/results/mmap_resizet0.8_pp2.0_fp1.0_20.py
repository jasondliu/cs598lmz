import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get the error
<code>OSError: [Errno 22] Invalid argument
</code>
If I change the mode to <code>r+</code> I get the error
<code>OSError: [Errno 9] Bad file descriptor
</code>
I tried changing <code>f.fileno()</code> to <code>f.fileno()+1</code> and <code>f.fileno()-1</code> but I get the error <code>OSError: [Errno 9] Bad file descriptor</code> in both cases.
According to https://docs.python.org/3/library/mmap.html, the <code>mmap</code> object is created from the <code>fileno()</code> method of a file object. The <code>fileno()</code> method of a file object returns an integer that represents the underlying file descriptor of the file.
I am guessing that the file descriptor is changed somehow by <code>f.truncate()</code>, but I am not sure.
