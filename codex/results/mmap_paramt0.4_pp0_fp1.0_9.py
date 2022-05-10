import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'
    print(m[0])
</code>
При выполнении получаю ошибку:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'0'
TypeError: must be read-write buffer, not mmap
</code>
Подскажите, пожалуйста, как исправить.

