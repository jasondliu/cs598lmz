import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

#
# The following are used to generate the protocol version string.
#

# The protocol version is the maximum of the supported versions.
PROTOCOL_VERSION = max(version.PROTOCOL_VERSIONS)

# The protocol version string is the protocol version followed by the
# protocol versions supported by this client.
PROTOCOL_VERSION_STRING = str(PROTOCOL_VERSION) + ','.join(
    str(v) for v in version.PROTOCOL_VERSIONS)

#
# The following are used to generate the user agent string.
#

# The user agent is the client name followed by the client version.
USER_AGENT = '%s/%s' % (version.CLIENT_NAME, version.CLIENT_VERSION)

# The user agent string is the user agent followed by the protocol version
# string.
