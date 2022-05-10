import _struct

from . import _bgp
from . import _util
from . import _value

from . import _const
from . import _enum


class BgpPathAttr(object):
    def get_length(self, value):
        raise NotImplementedError('%s not implemented' % sys._getframe().f_code.co_name)  # pylint: disable=protected-access
        return 0

    def to_bytes(self, value):
        raise NotImplementedError('%s not implemented' % sys._getframe().f_code.co_name)  # pylint: disable=protected-access
        return b''

    def from_bytes(self, value, length):
        raise NotImplementedError('%s not implemented' % sys._getframe().f_code.co_name)  # pylint: disable=protected-access
        return None


class BgpPathAttrUnrecognized(BgpPathAttr):
    def get_length(self, value):
        return len(value)
