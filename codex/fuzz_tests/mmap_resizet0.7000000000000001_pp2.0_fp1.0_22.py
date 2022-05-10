import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Выдаёт ошибку:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\mmap.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>


A:

Потому что <code>mmap</code> будет работать только со старым размером файла, сколько было при создании <code>mmap</code>. Когда вы укорачиваете его, то подложка уже некорректная
