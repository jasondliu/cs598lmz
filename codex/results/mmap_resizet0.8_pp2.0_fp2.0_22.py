import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.flush()
    m.close()

print(a)
</code>
Здесь создается файл с одним байтом, потом выделяется для него маппинг. Потом файл урезается, после чего байт маппинга считывается. Проблема в том, что на Python 3.5 и 3.6 ответ равен <code>b''</code>, т.е. байт пропал, а на 3.7 он
