import weakref

from . import _common
from .path import Path
from . import _datastructures
from ._compat import text_type
from ._compat import string_types
from .exceptions import UserWarning
from . import _exceptions
from . import _signals
from . import _helpers
from . import _compat
from . import _globals
from . import _logging
from . import _config

# note: this is here to avoid circular imports
from .app import App

# Global state
_request_ctx_stack = LocalStack()
ctx = LocalProxy(lambda: _request_ctx_stack.top)
request = LocalProxy(lambda: _request_ctx_stack.top.request)
session = LocalProxy(lambda: _request_ctx_stack.top.session)

#: the active application
current_app = LocalProxy(lambda: _request_ctx_stack.top.app)

#: the URL adapter used for the current state
url_adapter = LocalProxy(lambda: _request_ctx_stack.top.url_adapter)

#:
