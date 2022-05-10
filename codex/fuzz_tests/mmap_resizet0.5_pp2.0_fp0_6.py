import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
As you can see, I open the file for reading and writing in binary mode. Then I create the memory map on the file descriptor. After that I truncate the file. Then I try to access the memory map.
This fails with the following error:
<blockquote>
<p>Traceback (most recent call last):<br/>
    File "test.py", line 11, in <br/>
      a = m[:]<br/>
  ValueError: mmap can't extend file to larger than 2GB</p>
</blockquote>
Is there a way to do this?


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>If the file is larger than <code>&lt;code&gt;length&lt;/code&gt;</code>, the extra data is ignored. It is an error to specify a length longer than the file’s current size.</p>
</blockquote>
So, you can't do this.

