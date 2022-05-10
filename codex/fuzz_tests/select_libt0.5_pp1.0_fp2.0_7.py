import select
import socket
import sys
import threading
import time
import traceback

from . import __version__, _common
from . import _constants as constants
from . import _errors
from . import _file_transfer as file_transfer
from . import _networking as networking
from . import _options as options
from . import _util
from . import _winreg

# The maximum number of bytes to send in a single message.
MAX_MESSAGE_SIZE = 65536

# The maximum number of bytes to read from a socket at once.
MAX_RECV_SIZE = 65536

# The maximum number of bytes to send to a socket at once.
MAX_SEND_SIZE = 65536

# The maximum number of bytes to read from a file at once.
MAX_READ_SIZE = 65536

# The maximum number of bytes to write to a file at once.
MAX_WRITE_SIZE = 65536

# The maximum number of bytes to send in a single file transfer.
MAX_FILE_TRANSFER_SIZE = 65536

# The maximum number of bytes to send in
