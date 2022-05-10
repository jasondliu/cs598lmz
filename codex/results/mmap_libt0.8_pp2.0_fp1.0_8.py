import mmap
import re
import sys
import threading
from typing import List

from . import tag
from .utils import linesplit


class Message:
    """
    A parsed message.

    This is a named tuple. The fields are:

    ======== ===============================================
    Field    Description
    ======== ===============================================
    tags     tags of the line
    prefix   prefix of the line
    command  command of the line
    params   parameters of the line
    ======== ===============================================
    """
    __slots__ = ('tags', 'prefix', 'command', 'params')
    __doc__ = __doc__

    def __new__(cls, tags, prefix, command, params):
        return tuple.__new__(cls, (tags, prefix, command, params))

    def __init__(self, tags, prefix, command, params):
        # Python2
        self.tags, self.prefix, self.command, self.params = tags, prefix, command, params

    def __repr__(self):
        return 'Message(tags=%r, prefix=%r
