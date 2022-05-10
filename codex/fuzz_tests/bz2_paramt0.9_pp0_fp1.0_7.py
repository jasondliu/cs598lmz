from bz2 import BZ2Decompressor
BZ2Decompressor.decompress
```

```
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress
```

```
from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()
decompressor.decompress
```

次に読み込んだファイルのデータをバイナリとして処理するように`open()`関数にする。

```
with open(filename, 'rb') as fd:
    body = decompressor.decompress(fd.read())
```

`decompress`関数はデータを解凍する関数であり、一度解凍すると元にもどし解凍できない（新しいデータを解凍するときはBZ2Decompressorを作り直す必
