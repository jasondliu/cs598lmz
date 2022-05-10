import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting:
<code>Traceback (most recent call last):
  File "&lt;pyshell#32&gt;", line 6, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure how to get the mmap to update itself. I know this is possible with <code>mmap.resize()</code> but I want to do this using <code>f.truncate()</code> or something similar.
I'm using Windows 10 and Python 3.5.2.
Edit: I've tried <code>mmap.resize()</code> and it works, but I don't know how to specify the size to resize it to. I'm trying to resize to the size of the file, which is zero, but I don't know how to get that information.


A:

<code>mmap.resize</code> doesn't take a length in bytes, but rather the number of elements.
<code>m.resize(0)
</code>
Alternatively, you can close
