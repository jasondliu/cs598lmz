import types
types.ClassType = type
from types import ClassType
# To keep this module compatible with python 2.3, we have to do this.
from logging import DEBUG as LOG_DEBUG
from logging import INFO as LOG_INFO
from logging import WARN as LOG_WARN
from logging import ERROR as LOG_ERROR
from logging import CRITICAL as LOG_CRITICAL
from logging import FATAL as LOG_FATAL
from logging import addLevelName
from logging import getLevelName
from logging import isLevelBelow
from logging import isLevelBelow
addLevelName('ALL', 'ALL')
addLevelName('TRACE', 'TRACE')
from logging import getLevelName
from logging import isLevelBelow
from logging import setLevel
from logging import StreamHandler
from logging import FileHandler
from logging import Formatter
from logging import LogRecordFactory
from logging import fatal
from logging import error
from logging import warning
from logging import warn
from logging import info
from logging import log
from logging import debug
from logging import trace
from logging import set_trace
from logging import basicConfig
from logging import critical
from logging import log
from logging import getLogger
