import weakref
from exceptions import NotImplementedError
from robot.variables import is_scalar_var
from robot.utils import getdoc

from .executionqueue import ExecutionQueue
from .input import get_input
from .handlers import TRACE, DEFAULT_LOG_LEVEL, MessageHandler
from .utils import RERAISED_EXCEPTIONS, get_error_message, get_short_error_details, \
    get_full_message, get_error_details, IRONPYTHON, PY3

from .statistics import Statistics
from .statistics import SuiteStatistics
from .statistics import TestStatistics
from .statistics import KeywordStatistics


if PY3:
    import html
else:
    import htmllib


