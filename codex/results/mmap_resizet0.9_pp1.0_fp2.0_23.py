import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line of the script prints <code>None</code>, meaning <code>a</code> is actually <code>b''</code> when m.read() is called. Why?
It doesn't have to make sense to keep binary objects around... Removing them when they're no longer needed is just more efficient, right?


A:

<code>mmap</code> stores a reference to the file in order to check if it changes the file's size.
If you want to keep the <code>mmap</code> instance alive, you need to keep the file alive, too:
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
</code>

