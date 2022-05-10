import io
# Test io.RawIOBase as a baseclass
class CustomIO(io.RawIOBase):
    def read(self, n=-1):
        return b'A' * n

with CustomIO() as f:
    d = f.read(10)
    %preview d
    %preview d -f hex
    %preview d -f base64
    %preview d -f ascii

# Test io.BufferedIOBase as a baseclass
class CustomIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'A' * n

with CustomIO() as f:
    d = f.read(10)
    %preview d
    %preview d -f hex
    %preview d -f base64
    %preview d -f ascii

# Test BytesIO and TextIOBase
data = b'A' * 10
f = io.BytesIO(data)
f.seek(0)
%preview f
%preview f -n 1

data = "A" * 10
f = io.
