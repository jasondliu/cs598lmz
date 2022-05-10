import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>mmap.error: [Errno 22] Invalid argument</code>, because the file length is zero now and mmap can't map it anymore.
So, is there a way to achieve the same result without truncating the file?
I'd like to avoid creating a new file and doing a potential huge copy.


A:

You can do a <code>m.resize()</code> call on the <code>mmap</code> object to adjust the size of the <code>mmap</code> object. The object will still be usable, but any reads or writes outside the new bounds will raise <code>IndexError</code>.
The <code>resize()</code> call is only available in the <code>mmap</code> module in Python 3.3 and up; in earlier versions you'd have to create a new <code>mmap</code> instance.

