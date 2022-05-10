import weakref
import threading
import collections

from contexts import RequestContext as RequestContextBase
from contexts.exceptions import NotInContext


class RequestContext(RequestContextBase):
    """
    Stores all context variables.
    """
    _thread_locals = threading.local()

    @classmethod
    def get_request_context(cls):
        try:
            return cls._thread_locals.request_context
        except AttributeError:
            raise NotInContext()

    @classmethod
    def set_request_context(cls, request_context):
        cls._thread_locals.request_context = request_context

    @classmethod
    def remove_request_context(cls):
        try:
            cls._thread_locals.request_context = None
        except AttributeError:
            pass

    def __init__(self, request):
        self.request = request
        self.user = None
        self.session = {}
        self.application = None
        self.meta = {}

    def __enter__(self):
        self
