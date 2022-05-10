import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
вызывает <code>ValueError: NULL pointer access</code>.
Почему так происходит?
Как открыть <code>mmap</code> в таком случае, чтобы была та же самая картина, как на выбранном примере?


A:

Попробуйте указать режим <code>'w+'</code>:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.tr
