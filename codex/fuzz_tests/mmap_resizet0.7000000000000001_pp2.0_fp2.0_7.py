import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Выбрасывается ошибка <code>IndexError: string index out of range</code>. Однако если выполнить
<code>m.flush()
a = m[:]
</code>
то ошибка не выбрасывается. Почему при отсутствии flush() выбрасывается ошибка?
И ещё один вопрос. Если в моем коде заменить <code>f.truncate()</code> на <code>m.resize(0)</code> то ошибка не
