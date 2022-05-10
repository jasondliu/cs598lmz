import _struct

LOG_LEVEL_CRITICAL = 50
LOG_LEVEL_ERROR = 40
LOG_LEVEL_WARNING = 30
LOG_LEVEL_INFO = 20
LOG_LEVEL_DEBUG = 10
LOG_LEVEL_NOTSET = 0

LOG_LEVELS = {LOG_LEVEL_CRITICAL: 'CRITICAL',
              LOG_LEVEL_ERROR: 'ERROR',
              LOG_LEVEL_WARNING: 'WARNING',
              LOG_LEVEL_INFO: 'INFO',
              LOG_LEVEL_DEBUG: 'DEBUG'}

LOG_LEVEL_NAMES = {}
for k, v in LOG_LEVELS.items():
    LOG_LEVEL_NAMES[v] = k

class LogRecord(object):
    """A LogRecord instance represents an event being logged."""

    def __init__(self, name, level, pathname, lineno,
                 msg, args, exc_info, func=None):
        ct = time.time()
        self.name = name
        self.msg = msg
        self.args = args

