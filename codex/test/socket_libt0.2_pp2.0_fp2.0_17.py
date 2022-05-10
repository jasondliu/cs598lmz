import socket
import sys
import threading
import time

from . import config
from . import message
from . import util
from . import version

logger = logging.getLogger(__name__)

# The maximum number of bytes to read from a socket at a time.
MAX_READ_SIZE = 1024

# The maximum number of bytes to write to a socket at a time.
MAX_WRITE_SIZE = 1024

# The maximum number of bytes to read from a socket at a time when reading
# a message.
MAX_MESSAGE_READ_SIZE = 1024

# The maximum number of bytes to write to a socket at a time when writing
# a message.
MAX_MESSAGE_WRITE_SIZE = 1024

# The maximum number of bytes to read from a socket at a time when reading
# a message body.
MAX_MESSAGE_BODY_READ_SIZE = 1024

# The maximum number of bytes to write to a socket at a time when writing
# a message body.
MAX_MESSAGE_BODY_WRITE_SIZE = 1024

# The
