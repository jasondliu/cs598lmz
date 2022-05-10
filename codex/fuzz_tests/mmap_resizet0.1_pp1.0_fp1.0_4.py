import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I expected the output to be <code>b'\x01'</code>.
Why is the output <code>b'\x00'</code>?


A:

The <code>mmap</code> object is not updated when the file is truncated.
From the documentation:
<blockquote>
<p>The mmap() function is supported on Windows and most Unix systems. On
  Unix, it is implemented using the mmap() system call. On Windows, it
  is implemented using the CreateFileMapping() and MapViewOfFile()
  system calls.</p>
<p>The mmap() function is available on Unix and on Windows starting with
  Windows 2000. On Windows, mmap() can only be used to map files into
  memory. It cannot be used to map devices such as physical memory,
  ports, etc. On Windows, the file handle should not be closed while the
  mmap() object is still in use.</p>
</blockquote>

