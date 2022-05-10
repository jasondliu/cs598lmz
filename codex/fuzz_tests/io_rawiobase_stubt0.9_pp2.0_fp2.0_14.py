import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', close=True):
        super().__init__(file, mode, close,
                         lambda x: x._is_closed(),   # raw_is_closed
                         lambda enc: enc,            # raw_read
                         lambda data, enc: None,     # raw_write
                         lambda pos: pos,            # raw_seek
                         lambda enc: 0,              # raw_tell
                         lambda enc: None,           # raw_flush
                         lambda limit: None,         # raw_close
                         lambda size, enc: None,     # raw_truncate
                         lambda enc: False)          # _checkClosed

def x_fmt(v, i=None, z=''):
    """Format x value."""
    if i is not None:
        # Strip trailing zeros
        return ('%%.%sf' % i).rstrip('0') % v
    if z:
        # Append suffix
        return ('%%.%sf' % z).rstrip('0') % v
    return '%s' % v

def
