import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _util
from . import _compat
from . import _exception
from . import _file
from . import _file_system
from . import _path_spec
from . import _raw
from . import _resolver
from . import _serializer


class FileSystem(object):
  """Class that implements a file system."""

  def __init__(self, resolver_context=None):
    """Initializes a file system object.

    Args:
      resolver_context: optional resolver context (instance of resolver.Context).
    """
    super(FileSystem, self).__init__()
    self._file_system = None
    self._path_spec = None
    self._resolver_context = resolver_context

  def _Close(self):
    """Closes the file system object.

    Raises:
      IOError: if the close failed.
    """
    if self._file_system:
      self._file_system.Close()
      self._file_system = None

 
