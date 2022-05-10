import io
# Test io.RawIOBase.readinto()
r = io.BytesIO(b'*' * 10)
buf = bytearray(5)
r.readinto(buf)
r.readinto1(buf)

import os
# Test os.PathLike.readinto()
f = os.fsencode(__file__)
buf = bytearray(1)
