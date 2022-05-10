import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I am getting the following error:
<code>Traceback (most recent call last):
  File "C:/Users/xxx/PycharmProjects/xxx/test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I am using python 3.6.


A:

I think it's because you're closing the mmap object, but the file is still open.
You can use <code>m.resize()</code> to change the size of the mmap object, but then you have to re-initialize it with <code>m.seek(0,0)</code>

