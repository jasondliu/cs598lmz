import select
# Test select.select with a larger number of fds
# than the poll object can handle.
# See issue #1369 and issue #10066
# Poll objects have a limit of FD_SETSIZE.
# Some systems use a value of 1024, but that is not
# guaranteed.
# For this test we want FDs to be greater than that.
# We create a number of pipes.
# We use separate lists for the read and write ends.
# We set non-blocking mode on the write ends.
# We poll and check that the read ends are always readable.
# We poll and check that the write ends are always writable.
# We then set blocking mode on the write ends.
# We poll and check that the read ends are always readable.
# We write data to the write ends and check that the read ends
# become readable.
# We poll and check that the write ends are always writable.
# We then do a single select and check that the read and write
# ends are always readable and writable.
import unittest
from test import support
from unittest import mock
from select import select as sel
from select import _select
