import weakref

from . import _pynetworktables2
from . import _ntcore
from . import _networktables
from . import _networktables2
from . import _networktables_struct

from . import _networktables_struct
from ._networktables_struct import ConnectionInfo, EntryInfo, RpcCallInfo, RpcAnswerInfo, NotifyFlags


if sys.version_info[0] < 3:
    _string_types = (str, unicode)
else:
    _string_types = (str,)

def _check_string(s):
    if not isinstance(s, _string_types):
        raise TypeError("Argument must be a string")

def _check_string_or_none(s):
    if s is not None and not isinstance(s, _string_types):
        raise TypeError("Argument must be a string or None")

def _check_string_list(l):
    if not isinstance(l, list):
        raise TypeError("Argument must be a list of strings")
    for s in l
