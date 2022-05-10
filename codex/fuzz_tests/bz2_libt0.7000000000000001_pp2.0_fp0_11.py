import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import lzma
lzma.LZMAFile(filename)

import zipfile
zipfile.ZipFile(filename)

```

##### 보조 입력 스트림

```python
import io
with open('sample.bin', 'rb') as input:
    with io.BufferedReader(input) as buffered:
        pass

with open('sample.bin', 'rb') as input:
    with io.BufferedReader(input, buffer_size=1000) as buffered:
        pass

with open('sample.bin', 'rb') as input, open('sample.txt', 'w') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as wrapper:
        wrapper.write(input.read())

```

##### 기본 출력 스트림

```python
