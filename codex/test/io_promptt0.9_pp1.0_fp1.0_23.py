import io
# Test io.RawIOBase for presence of readinto method.
# NOTE(gazay): Python 2.6 io.RawIOBase is NOT a new-style class.
if hasattr(io.RawIOBase, 'readinto'):
    from io import RawIOBase
else:
    from collections import UserString  # noqa
    class RawIOBase(UserString):
        pass

