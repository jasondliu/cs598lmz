import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]   # после того, как будет попытка обратиться к файлу, живым будет только первый байт.
</code>
Также не забудьте про то, что при открытии файла в режиме <code>w</code>, если он существует, то он будет очищен.
В вашем случае можно использовать <code>r+</code>, 
