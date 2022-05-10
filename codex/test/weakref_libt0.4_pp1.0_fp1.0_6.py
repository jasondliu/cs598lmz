import weakref

from . import _util
from ._util import (
    _get_default_session,
    _make_method_return_future,
    _method_docs,
)
from .aiohttp_transport import AIOHTTPTransport
from .exceptions import (
    ClientError,
    Forbidden,
    HTTPException,
    NotFound,
    ServerError,
    Unauthorized,
)
