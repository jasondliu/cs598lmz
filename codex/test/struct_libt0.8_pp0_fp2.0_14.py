import _struct
import struct

from . import smb_structs

_ = i18n._

class SF(object):
    def __init__(self, f, default=None):
        self.f = f
        self.default = default
        if f is not None:
            if isinstance(f, SF):
                self.f = f.f
                self.name = f.name
                self.default = f.default
            else:
                if not isinstance(f, str):
                    self.f, self.name = f
                else:
                    self.name = f

    def unpack(self, data):
        if self.f is None:
            return self.default, data
        return unpack_data(data, self.f)

    def pack(self, data):
        if self.f is None:
            return EMPTY_BUFFER
        return pack_data(data, self.f)

    def __str__(self):
        if self.f is None:
            return '<SF None (default %r)>' % self.default
