import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(4096)
    m.close()
</code>
I get the error <code>mmap.error: [Errno 12] Cannot allocate memory</code>. What is the problem?


A:

It looks like this is a problem with the Python implementation of <code>mmap</code> on Windows.
In the Python source code (2.7.3), the <code>mmap.resize()</code> function calls the Windows API <code>SetFilePointer</code> to set the current file position. If the file position is greater than or equal to the current file size, it calls <code>SetEndOfFile</code> to increase the file size. If the file position is less than the current file size, it calls <code>SetFileValidData</code> to truncate the file.
So for a file that is smaller than 4096 bytes, <code>SetEndOfFile</code> should be called to increase the file size to 4096. However, the Python implementation of <code>SetEndOfFile</code> calls <code>SetFileInformationByHandle</code> with the <
