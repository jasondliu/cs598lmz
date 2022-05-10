import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = f.read()
    print(a, b)
</code>
При запуске программы выводится <code>b'' b'\x01'</code>, хотя я ожидал <code>b'\x01' b''</code>. Соответственно вопрос - почему поведение такое, а не иное?
Я видел информацию, что дело в том, что файловое место, которое выделено под строку, не сд
