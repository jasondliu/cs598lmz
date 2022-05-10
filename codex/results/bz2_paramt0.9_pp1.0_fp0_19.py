from bz2 import BZ2Decompressor
BZ2Decompressor
```

```
file = open('wikibooks.xml.bz2')
bzip_file = BZ2File(file)
bzip_file.read()
```

```
from bz2 import BZ2File
BZ2File
bz_com = BZ2Compressor()
bz_com
```

```
bz_com.compress(text)
bz_com.flush()
```

```
bz_decom = BZ2Decompressor()
bz_decom
bz_decom.decompress(bz_com.compress(text) + bz_com.flush()) == text
```
