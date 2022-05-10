import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.close()

print(a)
</code>
It works if you change <code>f.truncate()</code> to <code>m.truncate()</code>, but I thought that was the whole point of <code>mmap</code> -- to have shared access to the memory. 
I remember reading somewhere that you need to flush the file's buffers before truncating it, but I'm not sure where the buffers are for the file. Am I correct in thinking that the file's buffers are the same as the process' buffers?
It's also possible that I'm completely confused and this is working as it should.


A:

The file has no buffers, it's an OS layer below the process. Flushing buffers means that they are written to the OS as quickly as possible, to persist through crashes. 
The process has buffers. Your process has a buffer for the mmap contents. You modify the file through the mmap, but you don't read it again, so there's nothing to flush. Then you modify the file through the file descriptor, but there's no way to tell the OS to flush that buffer.
It's not clear
