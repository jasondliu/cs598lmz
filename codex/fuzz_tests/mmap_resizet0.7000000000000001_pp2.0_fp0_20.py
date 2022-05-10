import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>, which is confusing because the file is truncated.
What's the correct way to truncate the file?


A:

From the documentation:
<blockquote>
<p>After the original file is closed, modifications to the memory map are
  written back to the original file.</p>
</blockquote>
You need to close the file and reopen it to see the changes.

