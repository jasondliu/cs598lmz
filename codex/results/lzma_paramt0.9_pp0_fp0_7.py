from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
# b'data to decompress'
```

[Reference](https://docs.python.org/3/library/lzma.html)




### Decompress GZ

```python
# Decompress GZ
import lzma
import gzip
import tarfile

with tarfile.open('data.tar.gz') as tar:
    with tar.extractfile('data.txt.xz') as f:
        with lzma.open(f, mode='rt') as xz:
            with gzip.open(xz, mode='rt') as gz:
                text = gz.read()
                
print(text)
```



---

## CSV

```python
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
```

```
[['1', '26660114123', '2020-
