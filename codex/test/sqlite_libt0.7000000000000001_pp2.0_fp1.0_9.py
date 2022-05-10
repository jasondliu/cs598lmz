import ctypes
import ctypes.util
import threading
import sqlite3
import time
import uuid
from ssl import wrap_socket, CERT_NONE, PROTOCOL_TLSv1, SSLError

import requests
import requests.exceptions
from requests.packages.urllib3.util.ssl_ import (
    create_urllib3_context,
    HAS_SNI,
)

from .exceptions import (
    MetadataRetrievalError,
    ConnectionFailure,
    SSLCertVerificationError,
)
from .util import (
    is_unix,
    is_windows,
    is_mac,
    is_py2,
)

# ipv6_enabled is a global variable, which stores the value of
# whether IPv6 is enabled on the system
ipv6_enabled = False

# Set the global variable based on the OS
# We are not checking for linux, as we assume it supports IPv6
