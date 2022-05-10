import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
error :
<code>---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
&lt;ipython-input-7-de3a06f29373&gt; in &lt;module&gt;
      9 with open('test', 'r+b') as f:
     10     m = mmap.mmap(f.fileno(), 0)
---&gt; 11     f.truncate()
     12     a = m[:]
     13     print(a)

ValueError: mmap can't resize a file, mmaps can only be resized using mremap() which is only available on Linux, or MADV_REMOVE on OSX
</code>
I'm using ipython on mac.
How to truncate a file without mmap,or how to use mremap?

