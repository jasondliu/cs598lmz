import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Но мне не нравится то, что при использовании <code>mmap</code> нужно заранее знать размер файла. Можно ли как-то выделить память под маппинг, не зная размера файла?


A:

В документации к модулю <code>mmap</code> написано:
<blockquote>
<p>The optional length argument specifies the number of bytes to map. If
  length is omitted, the entire file is
