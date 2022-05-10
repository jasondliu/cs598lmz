import lzma
lzma.LZMACompressor
```

```
help(lzma)
```

```
import lzma
mdata = b"Random bytes as example data"
with lzma.open("file.xz", "w") as f:
    f.write(mdata)
```

```
import lzma
with lzma.open("file.xz") as f:
    file_content = f.read()
```

```
import lzma
with lzma.open("file.xz") as f:
    file_content = f.read(100)
```

```
import lzma
with lzma.open("file.xz", mode="wt", encoding="utf-8") as f:
    f.write("Content to compress")
```

```
import lzma
with lzma.open("file.xz", mode="wt", encoding="utf-8") as f:
    f.writelines(["foo\n", "bar\n"])
