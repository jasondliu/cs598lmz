import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Получаю ошибку:
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    a = m[:]
IndexError: mmap slice is past end of data
</code>
Делаю другой вариант для 32-х битной транспонированной матрицы (нижний индекс содержит смещение по строкам матрицы):
<code>with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
a = np.frombuffer(m,
