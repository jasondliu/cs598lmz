import io
# Test io.RawIOBase
if isinstance(io.RawIOBase(), io.RawIOBase):
    print('RawIOBase')
# Test io.BufferedIOBase
if isinstance(io.BufferedIOBase(), io.BufferedIOBase):
    print('BufferedIOBase')
# Test io.TextIOBase
if isinstance(io.TextIOBase(), io.TextIOBase):
    print('TextIOBase')
