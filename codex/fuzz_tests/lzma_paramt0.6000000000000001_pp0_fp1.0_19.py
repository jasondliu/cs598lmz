from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

from lzma import compress
compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)

from lzma import decompress
decompress(data, format=FORMAT_AUTO, memlimit=None)

from lzma import open
open(filename, mode="rb", format=FORMAT_XZ, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

from lzma import LZMAFile
LZMAFile(fileobj=None, mode="rb", filename=None, format=FORMAT_XZ, check=-1, preset=None, filters=None, bufsize=0)
```

```
from lzma import LZMA_OK
from lzma import LZMA_STREAM_END
from lzma import LZMA_NO_CHECK
from lzma import LZMA_UNSUPPORTED_CHECK
from lzma import LZMA
