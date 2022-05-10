import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
The line <code>m = mmap.mmap(f.fileno(), 0)</code> gives an error <code>OSError: [Errno 22] Invalid argument</code>.
On the other hand, running this script on python 3.4 does not give the error.
Can anybody explain the error and how I can fix it in python 3.3?


A:

The issue here is that you are passing <code>0</code> as the second argument to <code>mmap()</code>. This argument is supposed to be the size of the file; some systems will allow you to pass <code>0</code> here and have the map automatically adjust to whatever the file turns out to be, but on others, the size must be explicitly passed.
So you need to know the size of the file before you create the mapping. 
The proper way to do this is open the file, obtain the size, and then <code>truncate</code> down to <code>bytes(1)</code>:
<code>with open('test', 'r+b') as
