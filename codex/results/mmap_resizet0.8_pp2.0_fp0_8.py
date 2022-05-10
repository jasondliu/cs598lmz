import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
and when I run it I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
TypeError: mmap can't modify a readonly or copy-on-write memory map
</code>
How can I get around this without calling <code>os.unlink</code>? I also tried to call <code>open('test', 'w')</code> instead of <code>open('test', 'wb')</code> but got the same error.
I'm on Python 3.4.2 on Arch Linux.


A:

You don't need <code>os.unlink()</code> at all; <code>truncate()</code> by itself is enough.
Mind you, the way you're using <code>mmap</code> is not a good idea, because a file opened in text mode might apply some transformations, such as replacing newlines with <code>\n</code>, as well as possibly adding or removing an end-
