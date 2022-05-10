from bz2 import BZ2Decompressor
BZ2Decompressor.__bases__ = (object,)

from bitshuffle import h5
h5.__bases__ = (object,)

from ipyparallel import (
    Client, LoadBalancedView,
    DirectView, AsyncMapResult, AsyncResult)
Client.__bases__ = (object,)
LoadBalancedView.__bases__ = (object,)
DirectView.__bases__ = (object,)
AsyncMapResult.__bases__ = (object,)
AsyncResult.__bases__ = (object,)

from IPython.external.decorator import decorator
decorator.__bases__ = (object,)

from IPython.external.path import path
path.__bases__ = (object,)

from IPython.lib import pretty
pretty.__bases__ = (object,)

from IPython.utils.importstring import import_item
import_item.__bases__ = (object,)

from IPython.utils.reimport import reimport
reimport.__bases__ = (object,)

from IPython.utils.timing import
