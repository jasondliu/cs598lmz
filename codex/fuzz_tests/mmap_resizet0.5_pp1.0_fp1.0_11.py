import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # ValueError: mmap can't resize a readonly or copy-on-write (COW) mapping
    print(a)
</code>
Почему так происходит? Ведь документация гласит:
<blockquote>
<p>The mmap module provides a way of mapping files into memory. This is useful for many purposes; one example would be to allow a conventional Python program to be able to treat a large binary data file as an array of integers.</p>
</blockquote>
То есть я рассчитывал, что после <code>f.truncate()</code> будет просто пустой массив. Но вместо этого получаю оши
