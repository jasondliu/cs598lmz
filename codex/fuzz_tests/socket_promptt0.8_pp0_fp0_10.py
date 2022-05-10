import socket
# Test socket.if_indextoname()
try:
  print(socket.if_indextoname(1))
except ValueError:
  # No route to index
  pass

# Test socket.if_nametoindex()
try:
  print(socket.if_nametoindex('lo'))
except ValueError:
  # No interface with name
  pass
```

```
lo
1
```


### python
###### [python](http://docs.python.org/3/)

- C interface (`/usr/include/python3.2mu/`)
- `./configure --enable-shared`

```py
# test compile-time python version
import sys
sys.version_info
```

```
sys.version_info(major=3, minor=2, micro=5, releaselevel='final', serial=0)
```


### python-opencv
###### [python-opencv](http://opencv.willowgarage.com/wiki/)

- Python bindings
- `apt-get install python-opencv`

```
