import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Result:
<code>---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
&lt;ipython-input-21-a3a9c0e3b3f8&gt; in &lt;module&gt;()
      7     m = mmap.mmap(f.fileno(), 0)
      8     f.truncate()
----&gt; 9     a = m[:]

ValueError: mmap segment is smaller than the file
</code>
What's going on?
I'm using Python 2.7.5 on Ubuntu 16.04.


A:

<code>mmap.mmap</code> has a lot of corner cases in its behavior and it's very easy to get them wrong.
In your case, the mmap object you obtained has a maximum length of 0 (that's the value of <code>0</code> you passed to <code>mmap.mmap</code>).  However, the underlying file is actually 1 byte long.  When you try to read from mmap, it tries to read from the underlying file (and fails,
