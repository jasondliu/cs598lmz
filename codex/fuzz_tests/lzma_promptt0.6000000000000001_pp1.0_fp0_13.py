import lzma
# Test LZMADecompressor with multiple concatenated streams.
# The streams are concatenated using a simple format:
# - Stream count (1 byte)
# - Streams (Stream count times: Stream size, uncompressed size, LZMA stream)

class LZMAStream:
    def __init__(self, size, usize, stream):
        self.size = size
        self.usize = usize
        self.stream = stream

def make_lzma_streams(streams):
    buf = io.BytesIO()
    buf.write(struct.pack("B", len(streams)))
    for s in streams:
        buf.write(struct.pack("<II", s.size, s.usize))
        buf.write(s.stream)
    return buf.getvalue()

def make_stream(size, usize, data, props=b""):
    buf = io.BytesIO()
    buf.write(props)
    buf.write(lzma.compress(data))
    return LZMAStream(buf.tell(), usize, buf.get
