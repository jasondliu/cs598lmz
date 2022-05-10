import socket
# Test socket.if_indextoname()

[socket.if_indextoname(1), socket.if_indextoname(2)]
#['lo0', 'en0']

# Test socket.if_nameindex()

[x[0] for x in socket.if_nameindex()]
#['lo0', 'en0']

# Test socket.if_nameindex()

[x[1] for x in socket.if_nameindex()]
#[1, 2]

# Test socket.if_nametoindex()

socket.if_nametoindex('lo0')
#1

# Test socket.if_nametoindex()

socket.if_nametoindex('en0')
#2
```

## [version_info](https://docs.python.org/3/library/sys.html#sys.version_info)

```python
import sys

sys.version_info
#sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)

# Returns tuple

sys.version_
