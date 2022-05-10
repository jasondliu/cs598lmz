import mmap

from .abstract_file_source import AbstractFileSource
from .file_system_close_source import FileSystemCloseSource
from .file_system_open_source import FileSystemOpenSource
from .memory_map_source import MemoryMapSource
from .read_source import ReadSource


def readfile(filename, max_size=None, mmap=True):
    """
      Reads the contents of the given file into memory.
    """

    if filename is None:
        raise TypeError('Missing filename parameter.')

    if not isinstance(filename, six.string_types):
        raise TypeError("Expecting filename to be a string.")

    if mmap:
        file_source = MemoryMapSource(filename)
    else:
        file_source = FileSystemOpenSource(filename)

    if max_size is not None:
        file_source.limit(max_size)

    return file_source.read()
