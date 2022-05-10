import _struct
from . import mft
from . import path
from . import sf
from . import tz
from . import utils
from . import vbr
from . import vfs
from . import vlib


class NTFSException(Exception):
  """Base class for NTFS exceptions."""


class NTFSDecodingError(NTFSException):
  """Raised when decoding fails."""


class NTFSEncodingError(NTFSException):
  """Raised when encoding fails."""


class NTFSVolume(object):
  """A NTFS volume."""

  def __init__(self, file_object):
    """Initializes a NTFS volume object.

    Args:
      file_object: the file-like object to read the volume.
    """
    super(NTFSVolume, self).__init__()
    self._file_object = file_object
    self._boot_sector = None
    self._file_system = None

  def _ParseBootSector(self):
    """Parses the boot sector."""
