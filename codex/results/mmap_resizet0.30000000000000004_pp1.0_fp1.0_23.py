import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>. I expected <code>b'\x01'</code>.
Why is the output <code>b'\x00'</code>?


A:

The <code>mmap</code> object is not updated when the underlying file is truncated.
From the documentation:
<blockquote>
<p>The mmap() function is supported on Windows and most Unix systems. On
  Unix, it is implemented using the mmap() system call. On Windows, it
  is implemented using the CreateFileMapping() and MapViewOfFile()
  system calls.</p>
<p>...</p>
<p>The mmap() function is not part of the POSIX standard and is
  available on many Unix systems. On Windows, it is only available on
  Windows NT, and not on Windows 95/98/ME. On Windows, mmap() is
  emulation using the MapViewOfFile() function, and has the following
  known limitations:</p>
<ul>
<li>The file
