import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__
from . import __author__
from . import __license__
from . import __email__
from . import __url__
from . import __description__

from . import config
from . import utils
from . import logger
from . import exceptions
from . import commands
from . import cli
from . import __main__

from .config import Config
from .utils import Utils
from .logger import Logger
from .exceptions import Exceptions
from .commands import Commands
from .cli import Cli
from .__main__ import Main

__all__ = [
    '__version__',
    '__author__',
    '__license__',
    '__email__',
    '__url__',
    '__description__',
    'Config',
    'Utils',
    'Logger',
    'Exceptions',
    'Commands',
    'Cli',
    'Main',
]
