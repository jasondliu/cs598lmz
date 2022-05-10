import gc, weakref
import rpdb2
import platform
import ctypes
import ctypes.util

class SessionProxy(object):
    "Proxy for a rpdb2.CSession instance"
    _session_ref = None
    _lock = None

    def __init__(self, session):
        self._lock = threading.RLock()
        self._session = None
        self._session_ref = weakref.ref(session, self._on_session_close)

    def _on_session_close(self, ref):
        try:
            self._lock.acquire()
            self._session_ref = None
        finally:
            self._lock.release()

    def __getattr__(self, name):
        session = self._session_ref()
        if session is None:
            raise rpdb2.CExceptionAlreadyClosed()

        return getattr(session, name)

    def __repr__(self):
        session = self._session_ref()
        if session is None:
            return '<SessionProxy object at %s (no session)>' %
