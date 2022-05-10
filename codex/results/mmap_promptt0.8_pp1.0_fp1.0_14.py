import mmap
# Test mmap.mmap(0,1,prtot.PROT_READ) with a path that is not a filename.
m = mmap.mmap(0,1,prtot.PROT_READ|prtot.PROT_WRITE,mmap.MAP_SHARED,
              os.open("/dev/null",os.O_RDWR))
self.failUnlessEqual(m.readline(), None)
raise TestFailed("should have raised IOError")
except IOError: pass
except: raise


def test_pickle(self):
for n in xrange(pickle.HIGHEST_PROTOCOL + 1):
pickle.dumps(self.m, n)

if __name__ == '__main__':
test_main()
```
 
## `test_msilib.py`
 
Uses `importlib.machinery` to load `test.msi`
 
```python
from test import support
import importlib.machinery
import importlib.util
import os
import sys
import unittest
import zip
