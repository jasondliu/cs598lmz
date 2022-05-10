import gc, weakref
from . import get_config

# a weakref to the singleton instance
_instance = None

# The global setting
_config = None

# The default loggers
_loggers = None

# The default console formatter
_console_formatter = None

# The default file formatter
_file_formatter = None

# The default console handler
_console_handler = None

# The default file handler
_file_handler = None

def init_log(name="logger", config_file=None):
    """
    Initial the logger and return a singleton Logger object.
    """

    global _loggers
    global _config
    global _instance
    global _console_formatter
    global _file_formatter
    global _console_handler
    global _file_handler

    if _loggers is None:
        _loggers = {}

    if _config is None:
        _config = get_config(config_file)

    if _console_formatter is None:
        _console_formatter = logging.Formatter(_config.get
