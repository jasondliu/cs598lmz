import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
В этом случае на последней строке происходит ошибка:
<code>Traceback (most recent call last):
  File "C:\Users\kamys\Desktop\mmap.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>


A:

Проблема в том, что при уменьшении размера файла на диске слой <code>mmap</code> не может снизить размер <code>mmap</code>-объекта
