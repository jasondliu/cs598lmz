import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Results into:
<code>TypeError                                 Traceback (most recent call last)
&lt;ipython-input-11-bc3bc6292484&gt; in &lt;module&gt;()
      3     m = mmap.mmap(f.fileno(), 0)
      4     f.truncate()
----&gt; 5     a = m[:]

mmap.pyx in mmap.mmap.__getitem__ (mmap.c:3734)()

TypeError: slice indices must be integers or None or have an __index__ method
</code>
Here:
<code>&gt;&gt;&gt; a = m[:]
&gt;&gt;&gt; type(a)
&lt;class 'str_iterator'&gt;
</code>
It should be <code>mmap.mmap</code>, of course.
Any ideas?


A:

The solution was posted in comments by @user2357112. I'm just posting it here:
You can create an in-memory mmap using
