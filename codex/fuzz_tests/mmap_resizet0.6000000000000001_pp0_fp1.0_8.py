import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Во время выполнения последней строки программа падает с такой ошибкой:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Почему скопировать данные из объекта <code>mmap</code> нельзя, если он не пустой?

