fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
g_b = bytes(fn)
print(g_b)
```

- generate format string 


```python3
import struct

payload = struct.pack('!I', 0x0804863a)

print(payload)
```


- format string %p %p %p ...
- CVE-2014-6271 (bash) export SHELLOPTS=$'cmd-os-a'
