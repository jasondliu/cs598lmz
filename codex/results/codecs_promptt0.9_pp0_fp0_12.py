import codecs
# Test codecs.register_error()
from test import support
from test.support import bigaddrspacetest
import unittest
import struct
from functools import partial

# Check that a registered error handler gets called eventually
from test.support import script_helper

from test.support import captured_stdout


class UTF8Handler:

    def __init__(self, errors=None):
        pass

    def handle(self, exception):
        if not isinstance(exception, UnicodeDecodeError):
            raise TypeError("don't know how to handle %r"
                % exception.__class__.__name__)
        return ('-' * exception.end), exception.end


class UTF16Handler:

    def __init__(self, errors=None):
        pass

    def handle(self, exception):
        if not isinstance(exception, UnicodeDecodeError):
            raise TypeError("don't know how to handle %r"
                % exception.__class__.__name__)
        s = ('-' * (exception.end - exception.start))
        return s, exception.end



