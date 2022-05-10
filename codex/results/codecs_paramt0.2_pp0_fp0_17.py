import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import utils
from . import config
from . import exceptions
from . import constants
from . import __version__

from .utils import (
    get_logger,
    get_logger_name,
    get_logger_level,
    set_logger_level,
    set_logger_name,
    set_logger_format,
    set_logger_datefmt,
    set_logger_stream,
    set_logger_file,
    set_logger_filemode,
    set_logger_rotating,
    set_logger_backup_count,
    set_logger_max_bytes,
    set_logger_when,
    set_logger_interval,
    set_logger_utc,
    set_logger_propagate,
    set_logger_encoding,
    set_logger_delay,
    set_logger_handlers,
    set_logger_filters,
    set_logger_
