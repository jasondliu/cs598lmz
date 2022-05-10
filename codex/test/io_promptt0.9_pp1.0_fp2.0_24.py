import io
# Test io.RawIOBase
mem = io.BytesIO()

class memory(io.RawIOBase):
    def readinto(self, b: bytes) -> int:
        m.seek(len(b))
        return len(b)

    def write(self, b: bytes) -> int:
        m.write(b)
        return len(b)

m = memory()
