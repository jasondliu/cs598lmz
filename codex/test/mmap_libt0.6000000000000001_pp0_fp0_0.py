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
