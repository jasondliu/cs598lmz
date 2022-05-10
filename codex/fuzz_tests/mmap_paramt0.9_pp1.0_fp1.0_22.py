import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'Z'
</code>


A:

<code>r+b</code> означает, что объект открывается в режиме байтомода "использование заголовка и изменение содержимого", то есть исходный объект должен быть открыт для записи и должен существовать. Однако <code>with open('test', 'wb') as f</code>:
<code
