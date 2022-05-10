from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

```
# a simple solution
from bz2 import decompress
decompress(data)
```

# File I/O

## Reading from a file

```
with open('file.txt') as f:
    data = f.read()
```

`read()` is one of many instance methods provided by `file` objects, which also
include `readline()`, `readlines()`, `write()`, `writelines()`, `close()`,
`flush()`, `seek()`, and `tell()`.

`readline()` takes a single argument, an integer specifying the maximum number
of bytes to return.

`readlines()` returns a list containing the lines of text.

`file` names are interpreted relative to the current working directory.

`mode` is an optional argument that specifies whether the file is opened in
text or binary mode. Text mode (the default) will convert all line endings to
`\n`, and the `read()` method returns the file contents as a single string. In
binary mode the `\n
