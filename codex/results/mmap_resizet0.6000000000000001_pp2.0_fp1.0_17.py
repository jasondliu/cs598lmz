import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Получаю исключение:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 6, in &lt;module&gt;
ValueError: mmap length is zero
</code>
Но ведь длина должна быть не нулевой, поскольку в неё ещё ничего не записано. Что мне делать?


A:

Открывать файл в режиме <code>'r+b'</code>
