import _struct
import _io

from . import Base
from . import ffi
from . import _struct_
from . import _io_

class struct_f_handle_pair(Base):
    __slots__ = ('fsid', 'fh32')
    _fmt = b'(QI)'
    _typ = _struct.struct_f_handle_pair
    _fields_ = [('fsid', _io_.struct_fsid), ('fh32', _io_.uint32_t)]
    def __init__(self, fsid=None, fh32=None):
        Base.__init__(self)
        if fsid is not None:
            self.fsid = fsid
        if fh32 is not None:
            self.fh32 = fh32

class struct_f_handle(Base):
    __slots__ = ('handle_bytes',)
    _fmt = b'(32s)'
    _typ = _struct.struct_f_handle
    _fields_ = [('handle_bytes', _io_.int8_t
