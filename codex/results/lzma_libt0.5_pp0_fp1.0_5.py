import lzma
lzma.LZMAFile(fileobj=open('test.xz', 'rb'))

import bz2
bz2.BZ2File(fileobj=open('test.bz2', 'rb'))

import gzip
gzip.GzipFile(fileobj=open('test.gz', 'rb'))

import zipfile
zipfile.ZipFile(fileobj=open('test.zip', 'rb'))

import tarfile
tarfile.TarFile(fileobj=open('test.tar', 'rb'))

```

## 读写

```python
import lzma
lzma.LZMAFile(fileobj=open('test.xz', 'wb'), mode='w')

import bz2
bz2.BZ2File(fileobj=open('test.bz2', 'wb'), mode='w')

import gzip
gzip.GzipFile(fileobj=open('test.gz', 'wb'), mode='w')

import zipfile
zipfile.ZipFile(fileobj=
