import weakref

from . import _pyximport
from . import _pyximport_util
from . import _pyximport_hook

from . import _pyximport_importers

from . import _pyximport_importers

_pyximport_importers.install()


def install(inplace=False, language_level=None):
    """Install the pyximport hook into sys.meta_path.

    If inplace is True, then build in-place, i.e. build in the same directory
    as the source file.  Otherwise, build in a temporary directory.

    If language_level is not None, it should be the Python language level
    to use for building the .c file.  The default is to use the same language
    level as the one used to run pyximport.
    """

    if inplace:
        build_dir = None
    else:
        build_dir = _pyximport_util.get_build_dir()
