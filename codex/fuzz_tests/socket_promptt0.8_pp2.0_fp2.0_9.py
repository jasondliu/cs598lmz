import socket
# Test socket.if_indextoname():
socket.if_indextoname(1)

# Test socket.gethostbyname():
socket.gethostbyname("www.google.com")

# Test socket.if_nameindex():
socket.if_nameindex()

# Test socket.gethostname():
socket.gethostname()
```

### Usage on Linux
Just like OS X, all the functions tested return some data.

### Usage on Windows
On Windows all of them return the expected values, except for `if_nameindex()` which, for some reason, returns `[0]` instead of an array of index and name pairs. There is no `if_indextoname` on Windows, this is instead solved through `if_nametoindex` so that seems to work as expected.

## Conclusion
In general, all tests passed, but the `if_nameindex` test failed (as mentioned above). Since I don't use that function, I don't really care.

## Tested Versions
### Tested with the following environment:
* Python 3.7.2
* Vagrant 2.2.3
*
