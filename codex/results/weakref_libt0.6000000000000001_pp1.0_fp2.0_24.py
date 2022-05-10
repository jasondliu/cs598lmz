import weakref
import threading

_TLS = threading.local()


def get_current_session():
    """
    Return the current session.

    :returns: the current session
    :rtype: :class:`~nipyapi.nifi.models.ProcessorEntity`
    """
    if not hasattr(_TLS, 'session'):
        raise RuntimeError("no current session")
    return _TLS.session()


class Session(object):
    """
    A Nipyapi session object.

    A session is active for a thread, and allows the programmer
    to make api calls without having to provide the token on each
    call.

    :param token: the authorization token
    :type token: str
    """

    def __init__(self, token):
        self.token = token

    def __enter__(self):
        if hasattr(_TLS, 'session'):
            raise RuntimeError("nested session")
        _TLS.session = weakref.ref(self)
        return self

    def __exit__(self, *args
