import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
В этом примере при попытке считать из маппинга возникает исключение <code>ValueError: mmap offset is greater than file size</code>.
Как я понимаю, после вызова <code>f.truncate()</code> длина файла становится равна 0, а в маппинге остается старая длина файла, равная 1.
Как правильно сократить 
