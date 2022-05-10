import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import x509
from . import x509_store
from . import x509_types

from . import _nassl

# SSLv2 is not supported by OpenSSL 1.0.1+
_nassl.SSL_OP_NO_SSLv2 = 0x01000000

# SSLv3 is not supported by OpenSSL 1.0.1+
_nassl.SSL_OP_NO_SSLv3 = 0x02000000

# TLSv1.3 is not supported by OpenSSL 1.0.2+
_nassl.SSL_OP_NO_TLSv1_3 = 0x04000000

# TLSv1.2 is not supported by OpenSSL 1.0.1+
_nassl.SSL_OP_NO_TLSv1_2 = 0x08000000

# TLSv1.1 is not supported by OpenSSL 1.0.1+
_nass
