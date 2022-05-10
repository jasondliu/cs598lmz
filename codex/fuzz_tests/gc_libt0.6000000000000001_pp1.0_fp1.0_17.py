import gc, weakref

from .. import _imaging as core
from ._imaging import map_buffer, unmap_buffer
from ._util import isPath, isStringType
from ._binary import i8
from ._util import isPath, isStringType
from ._util import py_str
from ._util import isPy3

from ._util import isPy2

from ._util import isPy3

if isPy2:
    from itertools import imap as map

if isPy3:
    from collections.abc import MutableMapping
    basestring = str
else:
    from collections import MutableMapping


class ImagingCore(object):
    def __init__(self, width, height, mode):
        self.im = core.new(mode, (width, height))

    def __getattr__(self, id):
        return getattr(self.im, id)

    def __setattr__(self, id, value):
        if id == "im":
            self.__dict__[id] = value
        else:
            setattr(self.im, id,
