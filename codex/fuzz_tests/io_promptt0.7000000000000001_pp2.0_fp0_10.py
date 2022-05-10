import io
# Test io.RawIOBase by creating a raw I/O implementation that operates on an in-memory
# bytearray
# 这个类也可以用来实现文件的操作，比如把io.RawIOBase的read方法具体化为文件的读取，write方法具体化为文件的写入，这样做的好处是我们可以自定义一个类，比如实现了记录读写日志，自动转换为大写等一系列功能
class BytesIO(io.RawIOBase):

    def __init__(self, initial_bytes=None):
        self._buffer = bytearray(initial_bytes
