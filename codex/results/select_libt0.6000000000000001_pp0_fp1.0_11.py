import select
import socket
import sys
import time

from . import error
from . import log
from . import util
from . import x509
from . import x509name

from .util import ssl_

# verify_flags
#
# The flags below are not used by the client but are used in
# the server.

# Verify that the connection is authorized by the peer.
#
# If this flag is used, a callback should be set as well.
# See ssl.set_verify.
VERIFY_PEER = 0x1

# Verify that the connection is authorized by the peer.
#
# Unlike VERIFY_PEER, this flag only verifies that the
# certificate is valid, not that the connection is
# authorized.  This is useful for cases where the
# certificates are used simply to authenticate the
# peer.
#
# If this flag is used, a callback should be set as well.
# See ssl.set_verify.
VERIFY_PEER_NO_AUTH = 0x2

# Require a certificate on the peer.
VER
