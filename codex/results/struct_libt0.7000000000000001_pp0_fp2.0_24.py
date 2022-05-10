import _struct

def decode_string(x):
    if len(x) == 0:
        return None
    if isinstance(x, str):
        return x
    x = x.lstrip(b'\x00')
    return x

def unpack_varlen(f):
    pos = f.tell()
    val, = _struct.unpack('<H', f.read(2))
    if val & 0x8000 != 0:
        val = val & 0x7FFF
        val = val << 16
        val = val | _struct.unpack('<H', f.read(2))[0]
    return val, pos + val

class DbHeader(object):
    def __init__(self, f):
        f.seek(0)
        self.signature, self.version, self.filetype, self.reserved1, self.creation_year, self.creation_month, self.creation_day, self.creation_hour, self.creation_minute, self.creation_second, self.modification_year, self.modification_
