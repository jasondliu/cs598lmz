from bz2 import BZ2Decompressor
BZ2Decompressor.__init__("")

from gzip import GzipDecompressor
GzipDecompressor.__init__("")

from lzma import LZMADecompressor
LZMADecompressor.__init__("")
```

```
# _cffi_include.pyx
cdef extern from "fcntl.h":
    unsigned O_RDONLY "O_RDONLY"
    unsigned O_WRONLY "O_WRONLY"
    unsigned O_RDWR "O_RDWR"
    unsigned O_TRUNC "O_TRUNC"

    unsigned O_APPEND "O_APPEND"
    unsigned O_CREAT "O_CREAT"
    unsigned O_EXCL "O_EXCL"

    unsigned O_BINARY "O_BINARY"
    unsigned O_TEXT "O_TEXT"
    unsigned O_NOINHERIT "O_NOINHERIT"

    unsigned _O_SHORT_LIVED "0x1000L"
    unsigned _O_TEMPORARY
