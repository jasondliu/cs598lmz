import bz2
bz2.BZ2File.readline = bz2.BZ2File.readline
from bz2file import BZ2File

import re, sys
from warnings import warn

from os import makedirs
from os.path import exists, basename, join

from .encoding import open_file_with_utf8
from .utils import (error, warning, invalid_name_log,
                    parallel_for,
                    DEFAULT_CORPUS_NAME,
                    unescape_xml)

class StreamItem(object):
    """ The class for representing a stream item.

    The stream item consists of two dictionaries: the first for metadata,
    and the second for stream content. These dictionaries are represented
    by the :attr:`metadata` and :attr:`content` attributes.
    """
    # As a hack to get flush working, we're setting buffer large (so
    # buffer.write will always just return successfully) and then
    # flushing and counting on all the buffers to clear.
    def __init__(self, name, all_fields=False,
                 metadata_
