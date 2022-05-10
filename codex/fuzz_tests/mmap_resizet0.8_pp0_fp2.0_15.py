import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Код дает исключение:
<code>Traceback (most recent call last):
  File "C:/Users/i.sysoev/Desktop/test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Мне бы хотелось получить пустой массив. Есть возможность реализовать данное поведение?


A:

Самый простой вариант, это использовать <code>mmap.ACCESS_READ</code>
<code
