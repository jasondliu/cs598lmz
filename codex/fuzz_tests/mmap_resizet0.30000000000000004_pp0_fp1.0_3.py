import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an <code>IndexError</code> exception on the last line.
What I would like to do is to get the data that was in the file before truncating it. I tried to use <code>m.size()</code> instead of <code>0</code> in the <code>mmap</code> constructor, but it doesn't work.
I also tried to use <code>m.tell()</code> to get the size of the file, but it returns <code>0</code>.
I can't use <code>f.read()</code> because I don't know the size of the file.
I also tried to use <code>m.resize()</code> instead of <code>f.truncate()</code>, but it raises an <code>OSError</code> exception.
I'm using Python 3.5.3 on Windows 10.


A:

The problem is that you are creating a new <code>mmap</code> object with the same file descriptor, but the file descriptor is now associated with a different file.  You need to create a new <code
