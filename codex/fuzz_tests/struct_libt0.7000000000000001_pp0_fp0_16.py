import _struct

import numpy as np

from .. import raw
from .. import helpers
from .. import config
from .. import utils
from .. import constants
from .. import errors
from .. import structures
from .. import ffi

from ..helpers import _check_connection


class Certificate(helpers.OpenSSLErrorWrapper):
    """
    A wrapper around an :py:class:`OpenSSL.crypto.X509` instance
    to make it easier to use for certificate generation.

    .. automethod:: OpenSSL.crypto.X509.dump
    """

    def __init__(self, type, *args, **kwargs):
        self._backend = kwargs.pop('_backend', None)
        if self._backend is None:
            self._backend = backend

        self._x509 = self._backend.X509_new(self._backend, type, *args, **kwargs)

        if self._x509 == ffi.NULL:
            raise MemoryError("Error creating X509 object")

        self._x509 = ffi.
