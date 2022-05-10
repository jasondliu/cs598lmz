import io
# Test io.RawIOBase.readinto().
import _io
RawIOBase = _io.RawIOBase
print('io RawIOBase test')
'''
ISSUE: should have had args
base = RawIOBase()
buf = bytearray(5)
for i in range(5):
    try:
        base.readinto(buf)

