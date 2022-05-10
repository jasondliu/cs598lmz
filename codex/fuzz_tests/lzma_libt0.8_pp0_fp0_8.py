import lzma
lzma.decompress(open('/tmp/1.txt.lzma', 'rb').read())
```

```
$ python3 -c "import lzma; print(lzma.decompress(open('/tmp/1.txt.lzma', 'rb').read()))"
b'hello, world!\\n'
```

## 秘密を解くためのPythonスクリプト

```lzma_decode.py
#!/usr/bin/env python3
import lzma
import sys

if len(sys.argv) != 3:
    print('usage: lzma_decode.py <infile> <outfile>')
    sys.exit(1)

infile, outfile = sys.argv[1:3]
with open(infile, 'rb') as fin:
    with open(outfile, 'wb') as fout:
        fout.write(lzma.decompress(fin.read()))
```

##
