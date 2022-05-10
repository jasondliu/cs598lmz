import io
class File(io.RawIOBase):
  """Class that mimics the behavior of io.FileIO, but implements reading
  and writing with a SequenceFile object."""

  def __init__(self, filename, mode, seqfile=None):
    """Initializes the File object.

    Args:
      filename: path to the file.
      mode: any mode supported by FileIO (e.g. "rb", "wb").
      seqfile: SequenceFile object to use for reading/writing.  If None,
        a new SequenceFile will always be created when the File object
        is used, otherwise the given SequenceFile will be used.
    """
    self._filename = filename
    self._mode = mode
    self._seqfile = seqfile
    self._is_open = True
    self._cached_reader = None
    self._cached_writer = None
    self._cached_blocksize = None
    self._cached_compression = None
    self._cached_compression_codec = None

  def readable(self):
    """Implements io.RawIOBase.readable."""
    return self._
