import io
# Test io.RawIOBase
import select
# Test select.poll
import array
# Test array.array
import mmap
# Test mmap.mmap

from gevent.fileobject import (FileObject, FileObjectThread,
                               FileObjectBlock, FileObjectPosix)
from gevent.socket import socket as GreenSocket
from gevent.event import Event
from gevent.thread import allocate_lock
from gevent.testing import ExpectedException
from gevent.testing.timing import ExpectedTimeouts
from gevent.testing import params, main
from gevent.testing.util import TestCase, find_non_empty_string_buffer
from gevent import util as mod_util
from gevent import six


PREPARE_PATTERNS = ('', 'a', 'aa', 'aaa')
READ_PATTERNS = ('', 'a', 'aa', 'aaa')
# YES_SOCK_NAME_CACHE_SUPPORTS_CHARACTERS is an indication that the
# socket.socket.getsockname() result is identical between gevent
# and the default socket. It is used for testing caching.
