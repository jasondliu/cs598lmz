import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Is there a way to get the bytes that were in the file before truncating it?


A:

It seems that what you're trying to do is impossible. If you truncate a file, the data is gone.
You can do something like this:
<code>with open('test', 'rb') as f:
    old_data = f.read()

with open('test', 'w') as f:
    f.write('new data')
</code>

