import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = bytes(0)
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
Однако, если мы попробуем сделать то же самое с файлом, записанным при помощи <code>write()</code> команды в консоли:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = bytes(0)
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
То получим ошибку:
<code
