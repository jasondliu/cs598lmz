import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It raises an exception at the last line with the message: "mmap.error: [Errno 22] Invalid argument". I assume it's related to memory and stdout. 
I found a solution by replacing the last line with these two:
<code>a = m[:]
print(a)
</code>
So what is it about the <code>print</code> statement that makes this work?


A:

The <code>mmap</code> object has a method <code>find</code> which will return the offset of the first occurrence of the given search string
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    print(m.find(bytes(1)))
</code>

