import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_WRITE)
    m[:] = bytes(2)
    m.close()
</code>
After executing this code the file <code>test</code> contains 1.
I'd like to open a file in read-write mode and then be able to write from the mapped region. Is this possible?
I'm on Windows.


A:

You're running into weird lock semantics with the Python <code>mmap</code> module on Windows because it uses the <code>FILE_MAP_ALL_ACCESS</code> mapping access type. 
From the MSDN docs on <code>FILE_MAP_ALL_ACCESS</code>: 
<blockquote>
<p>The file handle that the hFile parameter specifies must be opened with the GENERIC_READ | GENERIC_WRITE access right. When opening the file, use the FILE_SHARE_READ bit of the dwShareMode parameter, along with any other bits that your program needs (FILE_SHARE_WRITE and FILE_SHARE_DELETE). If the file handle is opened for any access other than FILE_MAP_ALL_
