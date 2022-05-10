import weakref

from . import _base
from . import _compat
from . import _constants
from . import _errors
from . import _events
from . import _extensions
from . import _filters
from . import _geometry
from . import _image
from . import _list
from . import _magick_wand
from . import _pixel_wand
from . import _quantum
from . import _type_wand
from . import _version
from . import _wandtypes


__version__ = _version.VERSION
__version_info__ = tuple(_version.VERSION_INFO)

MAGICK_VERSION_INFO = _magick_wand.libmagick.MagickLibVersion()
MAGICK_VERSION = '.'.join(map(str, MAGICK_VERSION_INFO))


class WandLibraryVersionError(RuntimeError):
    """Raised when a library version is not compatible with the installed
    version of MagickWand.

    .. versionadded:: 0.1.10

    """


class Wand(object):
    """The ``Wand`` object is the top
