import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I got the following error:
<code>Traceback (most recent call last):
  File "mmap.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
My question is:

Why is the length of the <code>mmap</code> object zero after I truncate the file?
How can I access the content of the <code>mmap</code> object after I truncate the file?



A:

The <code>mmap</code> object is a view into the file, not a copy of the file. When you truncate the file to zero bytes, the <code>mmap</code> object is no longer pointing to a valid memory mapped region.
You can use the <code>mmap</code> object's <code>resize()</code> method to resize the <code>mmap</code> object.
<code>with open('test', 'r+b') as f:
    m = mmap.mm
