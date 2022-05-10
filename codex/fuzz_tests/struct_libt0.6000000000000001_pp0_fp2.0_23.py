import _struct

# from . import _cffi_backend as backend
from . import _ctypes_backend as backend


def _get_backend():
    # return _cffi_backend
    return _ctypes_backend


if backend.IS_LITTLE_ENDIAN:
    def _iter_unpack_from(fmt, buf):
        if not isinstance(fmt, str):
            fmt = fmt.format
        empty = object()
        offset = 0
        last_was_pad = False
        while offset < len(buf):
            if last_was_pad:
                last_was_pad = False
                continue

            c = fmt(offset)
            if c == 'x':
                offset += 1
                last_was_pad = True
                continue
            elif c in 'cbB?hHiIlLqQnNfd':
                size = struct.calcsize(c)
                yield struct.unpack_from(c, buf, offset)[0]
            elif c == 's':
                size = struct.calcs
