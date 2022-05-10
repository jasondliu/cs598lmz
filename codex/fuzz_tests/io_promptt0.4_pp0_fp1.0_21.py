import io
# Test io.RawIOBase

import unittest
import weakref

from test import support
from test.support import bigaddrspacetest

# A mixin defining tests common to all RawIOBase subclasses.
#
# Subclasses should define the following attributes:
# * rawio: an instance of the RawIOBase subclass under test
# * closed_msg: the string expected to be returned by rawio.closed_msg
# * readable: True iff the file is readable
# * writable: True iff the file is writable
# * seekable: True iff the file is seekable
# * seek_wo: True iff the file is seekable and supports seeking past the end
#   of the file
# * read_all_data: the data that should be returned by read()
# * read_some_data: the data that should be returned by read(100)
# * read_all_data_big: the data that should be returned by read() when
#   bigaddrspacetest is enabled
# * read_some_data_big: the data that should be returned by read(100) when
#   big
