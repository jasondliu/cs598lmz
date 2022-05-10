import socket
socket.if_indextoname(7)
# 'Wi-Fi'
```

Prints all of the network interfaces:

```python
for i in range(256):
    try:
        print(socket.if_indextoname(i))
    except OSError:
        pass
```

## `syscall`

There are three methods to use:

- `syscall.gettable(8)` - lists the syscalls table for the given architecture.
  `8` is for x86-64 and `4` is for x86.
- `syscall.get_args(257)` - gets the syscalls' args for the given syscall.
  Each key's value is a tuple of (arg name, arg type, optional).
- `syscall.get_name(17)` - gets the name of the given syscall.

```python
from syscall import *

# prints all of the syscalls' args:
for syscall in gettable(8):
    print(syscall)

# prints all of the unistd_t sy
