import mmap
import os
import tempfile
from xml.etree import cElementTree as ET
from xml.etree.ElementTree import QName

from .helpers import _cdata
from .helpers import _initcd
from .helpers import _nsmap
from .helpers import _nspath
from .helpers import _register_namespace
from .helpers import _setroot
from .helpers import _strip_ns
from .helpers import _tag_ns
from .helpers import _valid_namespaces


class Swid(dict):
    """
    Tool object to represent a SWID Tag operator.
    """

    def __init__(self, data=None):
        """
        Init method

        :param data: A dictionary holding the values
        :type data: dict

        :return: None
        """

        if data is None:
            data = {}

        super(Swid, self).__init__(data)

    def get(self, key, default=None):
        """
        Getter for values

        :param key: The name of the key to
