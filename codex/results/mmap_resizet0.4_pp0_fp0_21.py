import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This is the exception I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I know that <code>mmap</code> is not the right tool for this task, but I would like to know why this happens.


A:

The <code>mmap</code> object is not updated when you truncate the file.  It still thinks the file is the length it was when you created the <code>mmap</code> object.  You can see this by printing <code>m.size()</code> after truncating the file.
You can fix this by calling <code>m.resize()</code> after truncating the file.  If you want to make the file larger, you can just pass the new size to <code>resize()</code>.  If you want to make it smaller, you can pass the new size to <code>resize()</code> and then
