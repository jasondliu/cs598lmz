import _struct

from . import _utils
from . import _errors
from . import _exceptions
from . import _compat
from . import _constants
from . import _opcodes

__all__ = ['VirtualMachine']

_PY2 = sys.version_info[0] == 2

REGISTERS = ['ip', 'fp', 'sp', 'sb', 'ra', 'p0']

REGISTER_VALUES = {
    'ip': 0,
    'fp': 1,
    'sp': 2,
    'sb': 3,
    'ra': 4,
    'p0': 5,
}

TYPE_MAP = {
    1: _utils.c_byte,
    2: _utils.c_ushort,
    4: _utils.c_uint,
    8: _utils.c_ulonglong,
}

