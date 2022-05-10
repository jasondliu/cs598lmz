import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)
# mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import socket
import struct
import sys
import time
import traceback

# The number of bytes in the header.
_HEADER_SIZE = 20

# The number of bytes in the footer.
_FOOTER_SIZE = 4

# The maximum number of bytes in a message.
_MAX_MESSAGE_SIZE = 1000

# The number of bytes in a message.
_MESSAGE_SIZE = _MAX_MESSAGE_SIZE + _HEADER_SIZE + _FOOTER_SIZE

# The number of messages in the buffer.
_BUFFER_SIZE = 50

# The number of bytes in the buffer.
_BUFFER_BYTES = _MESSAGE_SIZE * _BUFFER_SIZE

# The number of bytes in the message header.
_MESSAGE_HEADER_SIZE = _HEADER_SIZE + _FOOTER_SIZE
