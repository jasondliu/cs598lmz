from _struct import Struct
s = Struct.__new__(Struct)
s.defaults = None
s.endianness = '@'


class Binding(object):
  """
  Provides access to native data types in a cross-platform way.
  """

  def __init__(self, filepath, mode, offset=0):
    """
    :param filepath: Path to file for native access.
    :type filepath: :class:`str`
    :param mode: File mode - either `'r'` or `'w'`.
    :param offset: Offset (in bytes) from the beginning of the file.
    :type offset: :class:`int`
    """
    self.filepath = filepath
    self.mode = mode
    self.offset = offset
    self.file = None
    self.open()

  def seek(self, addr):
    """
    Set the current location in the file.

    :param addr: Byte address.
    :type addr: :class:`int`
    """
    self.file.seek(self.offset + addr, io.SEEK_SET)

