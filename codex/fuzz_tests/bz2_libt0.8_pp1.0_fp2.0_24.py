import bz2
bz2.BZ2File('data/data.json.tar.bz2')
```

```python
import gzip
gzip.open('data/data.json.tar.gz')
```

```python
import zipfile
zipfile.ZipFile('data/data.json.zip')
```

```python
import rarfile
rarfile.RarFile('data/data.json.rar')
```

```python
import tarfile
tarfile.open('data/data.json.tar')
```
### Exporting

* Dumping Python objects

```python
import json
with open('data.json', 'w') as f:
    json.dump([1, 2, 3, {'4': 5, '6': 7}], f)
```

* Saving compressed data

```python
import bz2
with bz2.BZ2File('data.json.bz2', 'w') as f:
    f.write(b'[1, 2, 3, {"4": 5, "
