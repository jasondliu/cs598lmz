import weakref
from functools import lru_cache

from .collector import Collector
from .helpers import ForegroundColor, ANSIColor
from .scope import get_scope, Scope
from .scopes import ScopeType
from .parsing import ParsingContext, ParsingState
from .reporters import StructuredReporter, JsonReporter, GeneralReporter


class ApplicationContext(object):
    def __init__(self, config, entrypoint, args_collector=None):
        self.config = config
        self.entrypoint = entrypoint
        # self.state = State()
        self.entrypoint_scope = get_scope('entrypoint')
        self.app_scope = get_scope('app')
        self.args_collector = args_collector
        self.collector = Collector(config)
        self.reporter = None
        self._report_time = None

    def close(self):
        if self.reporter:
            self.reporter.finish()
            self.reporter.print_report(self._report_time)

