import select
import sys
import time
import traceback

from . import const
from . import log
from . import util
from . import version

# TODO:
# - add support for multiplexing multiple connections over a single
#   socket (useful for testing)
# - add support for SSL
# - add support for Unix domain sockets
# - add support for IPv6
# - add support for non-blocking connect
# - add support for non-blocking accept
# - add support for non-blocking send
# - add support for non-blocking recv
# - add support for non-blocking sendto
# - add support for non-blocking recvfrom
# - add support for non-blocking sendmsg
