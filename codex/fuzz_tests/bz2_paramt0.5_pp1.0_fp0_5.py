from bz2 import BZ2Decompressor
BZ2Decompressor

import sys

# Python 2/3 compatibility
if sys.version_info.major == 2:
    import Queue as queue
    from urllib2 import urlopen
    from urllib2 import HTTPError
    from urllib import quote_plus
else:
    import queue
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.parse import quote_plus

from . import constants
from . import exceptions
from . import utils
from . import __version__
from . import __url__
from . import __author__
from . import __email__
from . import __license__
from . import __copyright__
from . import __credits__
from . import __maintainer__
from . import __status__
from . import __doc__

from .constants import __all__ as constants_all
from .exceptions import __all__ as exceptions_all
from .utils import __all__ as utils_all

__all__ = ['__version__', '__url__', '__author__', '__
