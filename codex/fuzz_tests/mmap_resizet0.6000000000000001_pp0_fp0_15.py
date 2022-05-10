import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Но после этого выбрасывается исключение <code>OSError: [Errno 22] Invalid argument</code>.
Есть ли какой-то способ правильно закрыть файл, чтобы не выбрасывалось это исключение?


A:

Проблема решается просто перед вызовом <code>truncate</code> вызывать <code>flush</code>:
<code>with open('test', 'r+b') as f:
    m =
