import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected <code>a</code> to be an empty <code>bytes</code> object, but it is <code>b'\x01'</code>.
Why is that?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Windows, it is only supported on NTFS. On Unix, it is supported on
  most filesystems. On Mac OS X, it is supported on HFS+ and most other
  filesystems.</p>
<p>The mmap() function is available on most Unix versions. On Windows,
  mmap() is supported starting with Windows 95. On Windows, the file
  object must be opened with the <code>&lt;code&gt;os.O_RDWR&lt;/code&gt;</code> flag.</p>
</blockquote>

