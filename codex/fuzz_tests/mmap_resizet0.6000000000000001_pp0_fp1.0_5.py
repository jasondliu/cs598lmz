import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error
<code>ValueError: mmap can't enlarge memory maps beyond their original size
</code>
What I have tried:

Using the <code>access</code> parameter of <code>mmap</code>
Using the <code>offset</code> parameter
Using the <code>length</code> parameter

I am using Python 3.7.6 on Windows 10, if that matters


A:

From the documentation:
<blockquote>
<p>The size of a memory-mapped file is set when the file is opened with mmap.mmap(), and cannot be changed. <strong>To map more than the current size of a file, you can use the length parameter.</strong> The length parameter is the size of the mapping, not the size of the file. <strong>If the file is larger than the mapping, the extra data is ignored.</strong></p>
</blockquote>
So, if you open the file with a length of 1, you can't then map more than 1 byte.
If you want to map the whole file, pass <code>0</code> as the
