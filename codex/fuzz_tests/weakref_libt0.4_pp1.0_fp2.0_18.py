import weakref

from . import _ffi, _lib


class _SSLObject(object):
    """
    Wrapper around a _lib.SSL object.  It exists mostly to automatically
    set and clear the pyOpenSSL.ssl_set_ex_data_pyobj() when the SSL
    object is created and destroyed.  It also takes care of incrementing
    and decrementing the reference count of the SSL object.
    """

    def __init__(self, ssl):
        self._ssl = ssl

        # The _ex_data_idx attribute is set by the caller.  It is the index
        # of the pyOpenSSL.ssl_set_ex_data_pyobj() slot.
        self._ex_data_idx = None

        # The _app_data attribute is the object that is set by
        # set_app_data() and retrieved by get_app_data().
        self._app_data = None

    def __del__(self):
        self.unset_app_data()

    def get_app_data(self):
        return self._app
