import _struct

from . import _common
from . import _compat
from . import _errors
from . import _ffi
from . import _util
from . import _winreg
from . import _winreg_proto
from . import _winreg_util
from . import _winreg_types


class RegistryKey(_winreg_types.RegistryKey):
  """A handle to a Windows Registry key."""

  def __init__(self, handle, name, root_key=None, close_handle=True):
    """Initializes a new Registry key.

    Args:
      handle: The Windows Registry key handle (an integer).
      name: The name of the key (a string).
      root_key: Optional parent root key (instance of RegistryKey).
      close_handle: Optional boolean value to indicate the handle should
                    be closed when the object is destroyed. The default is
                    True.
    """
    super(RegistryKey, self).__init__(handle, name, root_key=root_key)
    self._close_handle = close_handle

