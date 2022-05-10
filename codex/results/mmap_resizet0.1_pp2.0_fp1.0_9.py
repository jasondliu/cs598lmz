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
I expected it to be <code>b'\x01'</code>.
Why is it so?


A:

The <code>mmap</code> object is not updated when the file is truncated.
From the documentation:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Windows, it can only be used when mmap_mode is read-only; on Unix,
  mmap_mode can be read-only, read-write, or copy-on-write.</p>
<p>The mmap() function is available on Unix and Windows. On Windows, it
  can only be used when mmap_mode is read-only; on Unix, mmap_mode can
  be read-only, read-write, or copy-on-write.</p>
<p>The mmap() function is available on Unix and Windows. On Windows, it
  can only be used when mmap_mode is read-only; on Unix, mm
