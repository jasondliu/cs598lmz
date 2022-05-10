import lzma
lzma.open('test.txt.xz')

import bz2
bz2.open('test.txt.bz2')

import zipfile
zipfile.open('test.txt.zip')

import gzip
gzip.open('test.txt.gz')

import tarfile
tarfile.open('test.txt.tar.gz')

import rarfile
rarfile.open('test.txt.rar')
```

### 并发

```python
import concurrent.futures

def func(x):
    return x * x

with concurrent.futures.ProcessPoolExecutor() as executor:
    future = executor.submit(func, 10)
    print(future.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(func, 10)
    print(future.result())

with concurrent.futures.ProcessPoolExecutor() as executor:
    future = executor.map(func, [1, 2, 3])
   
