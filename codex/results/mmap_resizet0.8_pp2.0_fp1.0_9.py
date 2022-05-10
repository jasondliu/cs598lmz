import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(m)
</code>
The above code will result in "ValueError: mmap scene is closed". 
What I want to know is: Why this code didn't raise a "ValueError: underlying buffer has been detached" since the mmap.mmap object is already detached from the file and underlying buffer.


A:

<blockquote>
<p>Why this code didn't raise a "ValueError: underlying buffer has been detached" since the mmap.mmap object is already detached from the file and underlying buffer.</p>
</blockquote>
It seems like it's more of a buffer overflow than a memory leak.  An <code>mmap</code> object is just a wrapper around something like the <code>mmap</code> system call.  That system call has no idea what the buffer is supposed to be used for.  It doesn't have the concept of a "file descriptor" or a "file" or "file name" or "file contents".  It just maps a file - in the OS's filesystem - into virtual memory.  It returns a pointer to the beginning of the chunk of memory but it
