import weakref
from ..util.compat import unicode_type

from .exceptions import *
from .retry import _translate_sqlalchemy_retryable_exceptions


def _raiser(exception):
    def _raiseit(*arg, **kw):
        exc = exception(*arg, **kw)
        exc.__traceback__ = sys.exc_info()[2]
        raise exc

    return _raiseit


def get_raise_on_exception(exc, dbapi_module):
    return _raiser(
        _translate_sqlalchemy_retryable_exceptions(
            dbapi_module,
            exc,
            "invalidate_connection",
            _InvalidatePoolError,
        )
    )


class ConnectionProxy(Connection):
    def __init__(self, inner, weak_instance, raise_on_disconnect):
        super(ConnectionProxy, self).__init__(  # noqa
            engine=inner._engine,
            _connection_cls=inner.__class__,
            _execution_options=
