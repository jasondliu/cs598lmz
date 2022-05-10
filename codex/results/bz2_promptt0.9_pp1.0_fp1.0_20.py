import bz2
# Test BZ2Decompressor's read method without a marker
with bz2.open("test.bz2", function='r') as t:
    print("Decompressed file:", file=sys.stderr)
    out_file = open('test_none.out', 'wb')
    while True:
        data = t.read(256)
        if data == b"":
            break
        out_file.write(data)
```

```shell
💻 ./bz2tool.py 
```

```console
❯ bzip2 -d test_none.out 
bzip2: Can't guess original name for test_none.out -- using test_none.out.out
❯ cat test_none.out.out 
BZh9
```

## Python

```python
import sys
import bz2
with bz2.open("test_none.out", function='r') as t:
    print("Decompressed file:", file=sys.stderr)
    out_file = open('test.out', 'wb')
