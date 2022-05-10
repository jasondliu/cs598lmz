import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ|mmap.PROT_WRITE, access=mmap.ACCESS_COPY)
    m[0] = 2
</code>
В итоге, в файле будет лежать байт <code>2</code>, а не <code>1</code>.
Пример из википедии:
<code>#!/usr/bin/env python
# -*- coding: utf8 -*-

import mmap

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write("Hello Python!\n".encode('utf-8'))

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file
