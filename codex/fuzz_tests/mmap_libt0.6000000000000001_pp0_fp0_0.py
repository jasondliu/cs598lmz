import mmap
import struct
import sys

from io import BytesIO
from collections import defaultdict
from . import constants

# from . import constants

__all__ = ['load_data', 'load_data_as_dict']

def load_data(fileobj):
    """
    Load data from the file-like object.

    :param fileobj: The file-like object which contains the data.

    :return: A list of ``(name, data)`` tuples.
    """
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements

    # -- Header --
    header = fileobj.read(struct.calcsize('>IHHI'))
    magic, version, num_entries, data_size = struct.unpack('>IHHI', header)
    if magic != constants.MAGIC:
        raise ValueError("Failed to read data: invalid magic number")
    if version != constants.VERSION:
        raise ValueError("Failed
