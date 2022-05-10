import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This will raise an error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
However, this will not:
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I suspect this is due to the fact that the file is opened in write mode in the second case, and thus the mapping is updated when the file is truncated. 
<code>mmap</code> documentation states that:
<blockquote>
<p>If mmap() is called on a file that is larger than the process’s address space, only the portion of the file that can be mapped will be mapped.</p>
</blockquote>
However, it is not clear what happens if the file is truncated.
My question is: why is the first case raising an error? Is it because the file is opened in read-only mode?


A:

The behavior is
