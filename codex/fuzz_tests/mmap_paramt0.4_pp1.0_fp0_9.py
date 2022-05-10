import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
При выполнении выдаёт ошибку:
<code>Traceback (most recent call last):
  File "C:/Users/Андрей/Desktop/test.py", line 8, in &lt;module&gt;
    m[0] = b'2'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
Как исправить?


A:

Вы не можете изменять данные в объекте <code>mmap</code> присваиванием, потому что это не поддержив
