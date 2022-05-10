import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import utils
from . import const
from . import parser
from . import core
from . import config
from . import tools
from . import exporter
from . import models
from . import const
from . import errors

from . import __version__
from . import __author__


__all__ = [
    'utils',
    'const',
    'parser',
    'core',
    'config',
    'tools',
    'exporter',
    'models',
    'const',
    'errors',
    '__version__',
    '__author__',
]
