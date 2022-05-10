import _struct
import array
from . import status, memory
from . import *
from . import _util
from . import _endian
from . import _memory
from . import _status


def _read_write(func):
    def inner(self, addr, data=None, timeout=None):
        if self.is_closed:
            raise IOError(_status.USB_ERROR_NOT_FOUND, "Device not found")
        if data is not None and not isinstance(data, (bytes, bytearray)):
            raise ValueError("data must be bytes, not %s" % type(data).__name__)
        if timeout is None:
            timeout = self._timeout
        elif not isinstance(timeout, int):
            raise ValueError("timeout must be an integer, not %s" % type(timeout).__name__)
        if addr is None:
            addr = self._addr
        elif not isinstance(addr, int) or addr not in (0, 2, 4, 6):
            raise ValueError("Invalid address %s", addr)
        else:
            self
