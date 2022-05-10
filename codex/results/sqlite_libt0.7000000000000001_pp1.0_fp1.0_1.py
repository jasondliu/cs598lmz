import ctypes
import ctypes.util
import threading
import sqlite3
import re
import sys

from ..common import cs
from ..exceptions import *
from ..log import *
from ..utility import *
from ..protocol import *
from ..server import *
from ..client import *
from ..config import *
from ..protocol.vrp import *
from ..messages import *
from ..M2Crypto import X509

from .SecureServer import SecureServer
from .SecureClient import SecureClient

from ..threadpool import ThreadPool


class SecureServerFactory(ServerFactory):
    """
    Tcp server factory for secure servers.

    @ivar ca: Certificate authority to use for authentication.
    @type ca: L{M2Crypto.X509.X509}
    @ivar key: Private key for server certificate.
    @type key: L{M2Crypto.Evp.PKey}
    @ivar cert: Server certificate.
    @type cert: L{M2Crypto.X509.X509}
    @ivar cacert: CA certificate.
    @type cacert: L{M2Crypto.X509
