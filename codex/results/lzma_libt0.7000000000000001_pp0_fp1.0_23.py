import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

# TODO: add support for lz4 and brotli

from typing import Union, Tuple, Optional
from hashlib import blake2b
from binascii import hexlify
from base64 import b64encode
from marshal import loads, dumps
from itertools import product
from pprint import pformat
from . import config as config_module
from . import exceptions as exceptions_module
from .config import Config
from .exceptions import *
from .utils import *

# TODO: Improve the performance of the object creation

class DeepNode:
    """
    Represents a node of the configuration tree.
    """

    def __init__(self, config: Config, path: Tuple = (), value: Any = None):
        """
        Initializes a new instance of the class.

        :param config: the configuration object
        :param path: the path of the node
        :param value: the value of the node
        """

        # Make sure
