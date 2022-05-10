import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Получим <code>ValueError: can't extend mmap beyond end of file</code> в строке <code>a = m[:]</code>. А если закомментировать <code>f.truncate()</code>, то <code>a[0] == 1</code>.
На гугл группах пишут, что в Python 2.7 работало без ошибок, но сейчас нужно читать всё до записи, или просто не трогать <code>f</code> после <code>
