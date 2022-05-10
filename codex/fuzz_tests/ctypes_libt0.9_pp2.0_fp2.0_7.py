import ctypes
ctypes.util.find_library("c")

# The `find_library` method isn't perfect. If it fails you are on your own.
```

If `c` or `libc.so` is found you are good to go. Otherwise you will need to provide
a path to the library.

```python
import sys
import os
sys.path.append(os.path.expanduser("~/workspace/arpreq/"))

from arpreq import arpreq

# test from arpreq import arpreq

IPs = [IP for IP in range(1, 126)]
MACs = [arpreq(str(IP))[0] for IP in IPs]

for i in range(len(IPs)):
    print(str(IPs[i]) + ": " + str(MACs[i]))
```
