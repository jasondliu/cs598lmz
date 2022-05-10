import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
What I want this code to do is to generate a memory map of the file, truncate the file but get the data the memory map is looking at.
After this code is executed the <code>m</code> is empty (<code>b''</code>) and the <code>a</code> is also empty (<code>b''</code>). I would prefer to not have to re-read the file after truncating it as that would be inefficient. 
Is there a way to keep the memory map viewing the file even after it has been truncated?


A:

Now I know what the problem is. 
When the file is truncated, the underlying file object is closed and later when the memory map tries to access the contents it can't because the file descriptor is closed. 
I found the answer here:
<blockquote>
<p>This is due to some low-level details of mmap on Unix. If you want to
  unmap earlier, one option is to use the mmap module's mmap.close_fd
  function, which unlinks the mmap object from an open file descriptor
