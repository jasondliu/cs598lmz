import _struct

from . import _common
from . import _compression
from . import _encryption
from . import _errors
from . import _util

#: The version of the format (an integer).
VERSION = 0x0200

#: The version of the format (a string).
VERSION_STR = "0.2"

#: The file identifier (a bytes object containing ASCII characters).
FILE_IDENTIFIER = b"CRYPT4GH"

#: The file identifier (a string).
FILE_IDENTIFIER_STR = FILE_IDENTIFIER.decode("ascii")

#: The size of the file identifier (an integer).
FILE_IDENTIFIER_SIZE = len(FILE_IDENTIFIER)

#: The size of the file header (an integer).
FILE_HEADER_SIZE = FILE_IDENTIFIER_SIZE + 4

#: The size of the file trailer (an integer).
FILE_TRAILER_SIZE = 16

#: The size of the box header (an integer).
BOX_HEADER_SIZE = 16

#: The size of
