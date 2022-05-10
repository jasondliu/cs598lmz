from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: data

from . import __version__
from . import __author__
from . import __license__
from . import __url__
from . import __doc__

from . import utils
from . import config
from . import logger
from . import exceptions
from . import cache
from . import plugins
from . import downloader
from . import extractor
from . import converter
from . import uploader
from . import notifier
from . import cleaner
from . import scheduler
from . import database
from . import api
from . import cli
from . import web
from . import daemon
from . import worker
from . import main

__all__ = [
    '__version__', '__author__', '__license__', '__url__', '__doc__',
    'utils', 'config', 'logger', 'exceptions', 'cache', 'plugins',
    'downloader', 'extractor', 'converter', 'uploader', 'notifier',
    'cleaner', 'scheduler', 'database', 'api', 'cli', 'web
