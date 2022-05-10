import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
What's going on here? Why does truncating the underlying file cause the mmap'ed memory region to be emptied?
Update In response to Oleksandr's answer, I'm able to continue using the file and the mmap after truncating:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))
with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    try:
        a = m[:]
    except ValueError:
        print('mmap length is zero')
for i in range(10):
    with open('test', 'r+b') as f:
        m = mmap.mmap(f.fileno(), 0)
        print(f.
