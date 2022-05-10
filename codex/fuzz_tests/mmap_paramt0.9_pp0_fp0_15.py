import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes('hello, world!', 'utf-8')
    print(m.read(50).rstrip(b'\x00').decode())

with open('test', 'rb') as f:
    print(f.readline())```

```bash-4.2$ python pickle_issue.py 
hello, world!
b'hello, world!'
```
