import weakref
from ..errors import InternalError

from . import abc
from . import arrays
from . import attrs
from . import context
from . import device
from . import generic
from . import storage
from . import statproxy
from . import system
from . import tags
from . import types
from . import utils
from .allocator import Free
from .utils import wrap_device_memory
from ._dtypes import register_dtype

# Logging option
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())

try:
    unicode
except NameError:
    unicode = str
