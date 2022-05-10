import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f  # <-- f is closed and disowned
view[0] = 0
```

## Reference

* [Python's internal buffer objects](https://docs.python.org/3/c-api/buffer.html)
* [Python's BufferedReader class](https://docs.python.org/3/library/io.html#io.BufferedReader)

## Keywords

`io`, `cffi`, `c`, `python buffer`, `python`, `python 3`, `python2`, `python3`, `bytearray`, `io.RawIOBase`, `io.BufferedReader`, `io.BufferedReader.readinto`, `io.BufferedReader.write`, `io.BufferedReader.seek`, `io.BufferedReader.tell`
