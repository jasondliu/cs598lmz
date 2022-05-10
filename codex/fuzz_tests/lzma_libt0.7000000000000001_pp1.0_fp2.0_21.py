import lzma
lzma.open("test.xz")

# lzma.open("test.xz", format=lzma.FORMAT_RAW)
# lzma.open("test.xz", format=lzma.FORMAT_XZ)
# lzma.open("test.xz", format=lzma.FORMAT_ALONE)
# lzma.open("test.xz", format=lzma.FORMAT_AUTO)
```

- lzma.open("test.xz", mode="r")

```python
import lzma
lzma.open("test.xz", mode="r")

# lzma.open("test.xz", mode="r", format=lzma.FORMAT_RAW)
# lzma.open("test.xz", mode="r", format=lzma.FORMAT_XZ)
# lzma.open("test.xz", mode="r", format=lzma.FORMAT_ALONE)
# lzma.open("test.xz
